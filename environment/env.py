'''
Ad Bidding Environment 

This modules provides an interactable environment for an ad-bidding system
which can run in CLI or GUI mode.
It allows the user to/agent to:
- interact with the environement, 
- bid on keywords, and 
- view the results.

To generalize real world scenario, author has used 26 alphabets as placeholders
for real world keywords available for bidding.
During one bidding cycle only 10 randomly selected keywords are available for bidding,
All the bid values are generated by using a noraml distribution around mean values.    

Author: RPSB
Version: 2.0

Functions:
- setup(): Initializes gloable parameters like available keywords and mean prices.
- step(bid_bool, keyword, bid_amount) : step through one bidding cycle.
- launch(): runs the environment, allowing for 10 bidding cycles

'''

import pygame
import random

# For GUI mode Switch
GUI_FLAG = True         # True : game runs in GUI mode 
# GUI_FLAG = False        # False: game runs in CLI mode


if GUI_FLAG:
    # game window
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.Font(None, 36)
    
    # setup game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ad Bidding Simulation")    
    


# initialize the bidding keywords
KEYWORDS = [chr(i) for i in range(65, 91)]  # ['A', 'B', ..., 'Z']

available_keywords = []
mean_prices = {}

def setup():
    '''
    Setup global parameters before first bidding cycle
    '''
    global mean_prices, available_keywords
    
    # mean_prices = {kw: random.randint(50, 150) for kw in KEYWORDS}  # Mean price for each keyword
    
    # randomly selected mean values for each KEYWORD
    mean_prices = {
        'A': 149, 'B': 92, 'C': 146, 'D': 119, 'E': 88, 'F': 66, 'G': 71, 'H': 69,
        'I': 91, 'J': 135, 'K': 133, 'L': 101, 'M': 61, 'N': 73, 'O': 110, 'P': 87,
        'Q': 66, 'R': 141, 'S': 71, 'T': 137, 'U': 91, 'V': 129, 'W': 147, 'X': 60,
        'Y': 64, 'Z': 56
    }
    
    # pick 10 random keywords for first cycle
    available_keywords = generate_available_keywords()

    
def get_available_keywords():
    return available_keywords

def generate_available_keywords():
    return random.sample(KEYWORDS, 10)

def generate_current_cost(keyword):
    '''
    Generate a current cost using a normal distribution around the mean price.
    '''
    mean_price = mean_prices[keyword]
    std_dev = mean_price * 0.2  # 20% of the mean price as standard deviation
    current_cost = max(1, random.normalvariate(mean_price, std_dev))  # Avoid negative prices
    return round(current_cost, 2)

def step(bid_bool, keyword = None, bid_amount = 0):
    '''
    Simulate a single step in bidding environment
    
    Parameters:
    - bid_bool (bool)   :  whether to place bid in this cycle.
    - keyword (str)     :  the keyword to bid on if placing a bid
    - bid_amount(float) :  the bid amount placed by the player.
    
    Returns:
    - bid_result_bool (bool)     : True if the bid has won, False otherwise
    - competitor_bid (float)   : if a bid is placed, return the simulated bid from the highest-bid competitor
    
    '''
    
    global available_keywords
    
    bid_result_bool = False
    competitor_bid = 0.0
    
    if not bid_bool:
        # if not bidding in this cycle
        # reset the available keywords
        available_keywords = generate_available_keywords()
        return bid_result_bool, competitor_bid
    
    if keyword not in available_keywords:
        raise ValueError(f"Keyword {keyword} is not available")
    
    competitor_bid = generate_current_cost(keyword) 
    
    if bid_amount > competitor_bid:
        bid_result_bool = True
    
    available_keywords = generate_available_keywords()
    return bid_result_bool, competitor_bid
        
    
   
def cli_mode():
    '''
    Command Line Interface mode.
    '''
    print("Welcome to the Ad Bidding CLI Simulation!")
    
    setup()
    
    while True:
        # Display keywords and ask the player to pick one
        print("\nAvailable Keywords:")
        print(get_available_keywords())
        
        decision = input("Do you want to participate in this bid-cycle? (YES/NO)\n  ").strip().upper()
        if decision == 'YES' :
            bid_bool = True
        else:
            bid_bool = False
        
        if bid_bool:                    # if user wants to BID
            # Get user input
            keyword = input("Pick a keyword to bid on (or type 'exit' to quit): ").strip().upper()
            
            # if user wants to QUIT or EXIT
            if keyword == 'EXIT' or keyword == 'QUIT':
                break
            # Other-wise get the keyword to bid on
            if keyword not in get_available_keywords():
                print("Invalid keyword! Try again.")
                continue
            
            # Ask player for a bid
            try:
                bid = float(input(f"Enter your bid for keyword '{keyword}': "))
            except ValueError:
                print("Please enter a valid bid amount.")
            
            # step into the bidding cycle 
            bid_result, sec_bid = step(bid_bool, keyword, bid)
            
            # report results
            if bid_result:
                print("You won the bid!")
                print(f"Second highest Bid was: {sec_bid}")
            else:
                print("You lost the bid.")
                 
        else:                           # if user does not want to bid -> SKIP
            step(bid_bool)
        
            

def gui_mode():
    '''
    Graphical Interface mode using Pygame.
    '''
    running = True
    selected_keyword = None
    bid_result = None
    sec_bid = 0
    player_bid = ''
    message = 'click SKIP for skipping this Bid Cycle!'
    keyword_rects = []
    
     # setup globals 
    setup()
    
    # Generate positions for keyword buttons
    def generate_rectangles():
        ''' update rectangles for the current available keywords'''
        keyword_rects = []        
        for i, keyword in enumerate(get_available_keywords()):
            x = 50 + (i % 10) * 70
            y = 300 + (i // 10) * 50
            rect = pygame.Rect(x - 10, y - 10, 50, 40)  # Button around each keyword
            keyword_rects.append((keyword, rect))
        return keyword_rects
    
    keyword_rects = generate_rectangles()
    # DEBUG
    # print(keyword_rects) 
    
    # skip button:
    skip_button_rect = pygame.Rect(600, 200, 100, 40)
    
    # draw text on GUI
    def draw_text(text, x, y, color=BLACK):
        '''Utility function to draw text on the screen.'''
        label = FONT.render(text, True, color)
        screen.blit(label, (x, y))
    
    
    while running:
        screen.fill(WHITE)
        
        # display available keywords:
        draw_text(message, 50, 50)
        
        draw_text("Avaiable Keywords:", 50, 150)
       
        # Draw keywords as buttons
        for keyword, rect in keyword_rects:
            pygame.draw.rect(screen, BLACK, rect, 2)  # Draw box around keyword
            draw_text(keyword, rect.x + 10, rect.y + 5)
        
        # draw SKIP button
        pygame.draw.rect(screen, BLACK, skip_button_rect)
        draw_text("SKIP", skip_button_rect.x+20, skip_button_rect.y+10, WHITE)
        
        # show result of last bid if applicable
        if bid_result is not None:
            if bid_result:
                draw_text("You won the bid!", 50, 500)
                draw_text(f"Second highest bid was: {sec_bid}", 50, 530)
            else:
                draw_text("You lost the bid.", 50, 500)
        
        # Display current keyword and bid input box if a keyword is selected
        if selected_keyword:
            draw_text(f"Selected Keyword: {selected_keyword}", 50, 400)
            draw_text("Enter your bid:", 50, 450)
            draw_text(player_bid, 300, 450)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if selected_keyword:
                    if event.key == pygame.K_RETURN:
                        # Place bid
                        try:
                            bid_amount = float(player_bid)    
                        except ValueError:
                            message = "Invalid bid amount."
                        
                        bid_result, sec_bid = step(True, selected_keyword, bid_amount)
                        keyword_rects = generate_rectangles
                        # message = "Do you want to participate in this bid cycle?"
                        
                        player_bid = ''
                        selected_keyword = None
                        
                    elif event.key == pygame.K_BACKSPACE:
                        player_bid = player_bid[:-1]
                    
                    else:
                        player_bid += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                
                # Check if any keyword was clicked
                for keyword, rect in keyword_rects:
                    if rect.collidepoint(mouse_x, mouse_y):
                        selected_keyword = keyword
                        player_bid = ''  # Reset bid input when new keyword is selected
                
                # Check if the "Skip" button was clicked
                if skip_button_rect.collidepoint(mouse_x, mouse_y):
                    bid_result, sec_bid = step(False)
                    setup()  # Generate new keywords for the next cycle
                    keyword_rects = generate_rectangles()  # Update the keyword_rects to reflect new keywords
                    message = "New keywords generated for next cycle."

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    
    if GUI_FLAG:
        print(f"#__Runnning the Environment in GUI mode__#")
        gui_mode()
    else :
        print(f"#__Runnning the Environment in CLI mode__#")
        cli_mode()

    