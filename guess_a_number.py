import random
import streamlit as st

def get_random_number():
    return random.randrange(10, 90)

def give_hint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "❄️ Cold"
    elif number == guess:
        return "🎉 Correct!"
    else:
        return "🔥 Hot"

def run_guess_game():
    st.title("Number Guessing Game")
    st.write("Guess a number between 1 and 100")
    
    with st.expander("How to Play"):
        st.write("""
        - Try to guess the secret number between 1-100
        - You'll get hints after each guess:
          - ❄️ **Cold**: Your guess is more than 10 away from the secret number
          - 🔥 **Hot**: Your guess is within 10 of the secret number
          - 🎉 **Correct**: You guessed the exact number!
        """)
    
    # Initialize session state
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = get_random_number()
        st.session_state.last_guess = None
        st.session_state.last_hint = None
        st.session_state.game_over = False
    
    # Input for user's guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    # Guess button
    if st.button("Submit Guess"):
        if st.session_state.game_over:
            st.warning("You already won! Restart to play again.")
        else:
            hint = give_hint(st.session_state.secret_number, guess)
            st.session_state.last_guess = guess
            st.session_state.last_hint = hint
            
            if hint == "🎉 Correct!":
                st.session_state.game_over = True
    
    # Display the last guess hint
    if st.session_state.last_hint:
        st.write(f"Your guess {st.session_state.last_guess}: {st.session_state.last_hint}")
        
        if st.session_state.game_over:
            st.balloons()
            st.success("Congratulations! You guessed the right number!")
    
    # Restart button
    if st.button("Restart Game"):
        st.session_state.secret_number = get_random_number()
        st.session_state.last_guess = None
        st.session_state.last_hint = None
        st.session_state.game_over = False
        st.rerun()

if __name__ == '__main__':
    run_guess_game()
