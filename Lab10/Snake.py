import pygame
import random
import psycopg2

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0
        self.paused = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        if not self.paused:
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)

# Game functions
def main():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Daymino220304.z"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user_score(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        score INTEGER
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS "user"(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        level INTEGER
    )""")

    # Prompt user for username
    username = input("Enter your username: ")

    # Check if user exists
    cursor.execute("SELECT * FROM \"user\" WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        print(f"Welcome back, {username}!")
        print(f"Your current level: {user[2]}")
    else:
        # Create new user
        cursor.execute("INSERT INTO \"user\" (username, level) VALUES (%s, %s)", (username, 1))
        print(f"Welcome, {username}!")

    # Set up the game
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
        # Get current level
        cursor.execute("SELECT level FROM \"user\" WHERE username = %s", (username,))
        level = cursor.fetchone()[0]

        # Game logic
        snake.handle_keys()
        snake.move()

        # Check if snake hits the borders
        if snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= SCREEN_WIDTH or snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= SCREEN_HEIGHT:
            snake.reset()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        # Drawing
        SCREEN.fill(BLACK)
        snake.draw(SCREEN)
        food.draw(SCREEN)

        # Display score and level
        score_text = font.render(f"Score: {snake.score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (10, 50))

        pygame.display.update()

        # Pause and save current state and score to database
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            cursor.execute("UPDATE user_score SET score = %s WHERE username = %s", (snake.score, username))
            cursor.execute("UPDATE \"user\" SET level = %s WHERE username = %s", (level, username))
            print("Game paused. Current state and score saved to database.")
            print("Press SPACE again to resume.")
            pygame.display.update()
            while True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    break

        # Level up based on score
        if snake.score >= 5 and level == 1:
            cursor.execute("UPDATE \"user\" SET level = 2 WHERE username = %s", (username,))
            print("Congratulations! You've reached Level 2!")
        elif snake.score >= 10 and level == 2:
            cursor.execute("UPDATE \"user\" SET level = 3 WHERE username = %s", (username,))
            print("Congratulations! You've reached Level 3!")
        
        clock.tick(8 + (level * 2))  # Speed increases with level

if __name__ == "__main__":
    main()
