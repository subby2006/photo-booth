import pygame
# import camera_view
import cv2
import sys
import numpy as np
# import test_mode

# Initialize Pygame
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("CrosseBooth")

# Function to display loading screen
def show_loading_screen():
    screen.fill((0, 100, 0))
    
    # Load loading image
    loading_image = pygame.image.load("assets/crosse_loading.png")
    loading_rect = loading_image.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(loading_image, loading_rect)

    # Loading text
    font = pygame.font.Font(None, int(screen_height * 0.05))
    loading_text = font.render("Loading...", True, (255, 255, 255))
    loading_text_rect = loading_text.get_rect(center=(screen_width // 2, screen_height // 2 + int(screen_height * 0.05)))
    screen.blit(loading_text, loading_text_rect)

    pygame.display.flip()

def draw_error_message(message):
    # Hide previous elements
    screen.fill((0, 0, 0))

    # Draw white box in the center
    box_width = screen_width // 1.5
    box_height = screen_height // 4
    box_x = (screen_width - box_width) // 2
    box_y = (screen_height - box_height) // 2
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))

    # Render and show the error message
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    

# def camera_test(): # don't use this yet, make sure main function works before moving to error handling
    # cap = cv2.VideoCapture(0)
    # if not cap.isOpened():
        # print("Camera module not found.")
        # draw_error_message("ERROR: Camera module not found.")
        # pygame.time.wait(5000)
        # pygame.quit()
    # else:
        # cap.release()
 
def main():    
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press the button to begin.", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    version_font = pygame.font.Font(None, 24)

    version_text = version_font.render("CrosseCam Version 1.0. Designed and Developed by Subhayan", True, (255, 255, 255))
    version_rect = version_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(version_text, version_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    waiting = False
    
    show_loading_screen()
    captured_frame = camera_view()
    show_frame(captured_frame) # WORKS!!!


    
def camera_view():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    # Get camera frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Load assets
    arrow_left = pygame.image.load("assets/arrowleft.png")
    arrow_right = pygame.image.load("assets/arrowright.png")
    red_button = pygame.image.load("assets/redbutton.png")

    # Get dimensions of the arrow images
    arrow_width = arrow_left.get_width()
    arrow_height = arrow_left.get_height()
    
    # button_width = int(red_button.get_width() * 0.25)
    # button_height = int(red_button.get_height() * 0.25)

    # Arrow image pos
    arrow_left_x = (screen_width - frame_width) // 2 - arrow_width - 10
    arrow_right_x = (screen_width + frame_width) // 2 + 20
    arrow_y = 50
    
    # Red button image pos
    # red_button_x = (screen_width - button_width) // 2
    # red_button_y = screen_height - 100 - button_height
    red_button_x = screen_width // 2 - red_button.get_width() // 2
    red_button_y = screen_height - 50 - red_button.get_height()
    
    # Calculate position to center camera feed on the screen
    cam_x = (screen_width - frame_width) // 2
    cam_y = (screen_height - frame_height) // 2

    # pygame.mixer.init()
    # capture_sound = pygame.mixer.Sound("assets/capture.wav")

    # Initialize captured frame
    captured_frame = None

    # Main loop to capture and display camera feed
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame from camera.")
            draw_error_message("ERROR: Error reading frame from camera.")
            break
            pygame.time.wait(5000)
            pygame.quit()

        # Convert frame to Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        
        # Clear the screen with dark green color
        screen.fill((0, 100, 0))

        # Display captured frame - don't use this
        #if captured_frame is not None:
            #screen.blit(captured_frame, (cam_x, cam_y))
        #else:
            #screen.blit(frame, (cam_x, cam_y))

        # Display camera feed
        screen.blit(frame, (cam_x, cam_y))

        # Display arrow images next to "Look at the birdie" message
        screen.blit(arrow_left, (arrow_left_x, arrow_y))
        screen.blit(arrow_right, (arrow_right_x, arrow_y))

        # Display message at the top of the screen
        font = pygame.font.Font(None, 48)  # Larger font size
        text = font.render("Look at the birdie", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, 50))
        screen.blit(text, text_rect)

        # Display red button image
        screen.blit(red_button, (red_button_x, red_button_y))

        # Display message at the bottom of the screen
        font = pygame.font.Font(None, 48)
        text = font.render("Press the button to capture", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height - 50))
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # capture_sound.play()
                    captured_frame = frame.copy()
                    print("Frame captured.")
                    cap.release()
                    return captured_frame
                
def show_frame(frame):
    # Display the captured frame along with a question
    screen.fill((0, 100, 0))  # Clear the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Does this look good?", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, 50))
    screen.blit(text, text_rect)
    # Display the captured frame
    if frame is not None:
        frame_rect = frame.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(frame, frame_rect)

    # Display Yes/No question at the bottom of the screen
    font = pygame.font.Font(None, 36)
    text_yes = font.render("Yes (up)", True, (255, 255, 255))
    text_yes_rect = text_yes.get_rect(center=(screen_width // 4, screen_height - 50))
    screen.blit(text_yes, text_yes_rect)
    text_no = font.render("No (down)", True, (255, 255, 255))
    text_no_rect = text_no.get_rect(center=(3 * screen_width // 4, screen_height - 50))
    screen.blit(text_no, text_no_rect)
    pygame.display.flip()

    # Wait for user response
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    style_selector(frame)
                    waiting = False
                elif event.key == pygame.K_d:
                    main()  # Return back to the camera view function
                    waiting = False

def style_selector(frame):
    styles = ["painting", "anime", "sketch", "fantasy", "none"]

    # Draw the main box
    box_width = 400
    box_height = 300
    box_x = (screen_width - box_width) // 2
    box_y = (screen_height - box_height) // 2
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))

    # Draw the title
    font = pygame.font.Font(None, 48)
    message = font.render("Choose a style", True, (0, 0, 0))
    message_rect = message.get_rect(center=(screen_width // 2, box_y + 20))
    screen.blit(message, message_rect)

    # Draw the style options
    font = pygame.font.Font(None, 36)
    text_y = box_y + 20
    selected_index = 0
    for index, style in enumerate(styles):
        text_color = (0, 0, 0) if index != selected_index else (255, 0, 0)
        text = font.render(style.capitalize(), True, text_color)
        text_rect = text.get_rect(center=(screen_width // 2, text_y))
        screen.blit(text, text_rect)
        text_y += 50

    pygame.display.flip()

    # Wait for user response
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "none"  # Quitting, default to "none" style
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    selected_index = (selected_index + 1) % len(styles)
                elif event.key == pygame.K_w:
                    selected_index = (selected_index - 1) % len(styles)
                elif event.key == pygame.K_z:
                    # return styles[selected_index, frame]
                    selected_style = styles[selected_index]
                    # return selected_style, frame
                    apply_style(selected_style, frame)
                
        pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))
        text_y = box_y + 20
        for index, style in enumerate(styles):
            text_color = (0, 0, 0) if index != selected_index else (255, 0, 0)
            text = font.render(style.capitalize(), True, text_color)
            text_rect = text.get_rect(center=(screen_width // 2, text_y))
            screen.blit(text, text_rect)
            text_y += 50

        pygame.display.flip()

def apply_style(selected_index, frame):
    if selected_index == "none":    
        print("none")
        show_thankyou(frame)
    elif selected_index == "painting":
        print("painting")

    elif selected_index == "anime":
        print("anime")
    
    elif selected_index == "sketch":
        print("sketch")

    elif selected_index == "fantasy":
        print("fantasy")

def show_thankyou(frame):
    screen.fill((0, 100, 0))  # Clear the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Looks good", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, 50))
    screen.blit(text, text_rect)
    # Display the captured frame
    if frame is not None:
        frame_rect = frame.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(frame, frame_rect)

    font = pygame.font.Font(None, 36)
    text_yes = font.render("Thank you for using CrosseBooth", True, (255, 255, 255))
    text_yes_rect = text_yes.get_rect(center=(screen_width // 2, screen_height - 50))
    screen.blit(text_yes, text_yes_rect)
    pygame.display.flip()
    pygame.time.delay(5000)
    main()

    # do something for the thumbs up image
    

# Run the game
if __name__ == "__main__":
    main()

# Quit Pygame
# pygame.quit()