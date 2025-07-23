# Number-Guessing-Game
Streamlit number guessing game with smart hot/cold hints, edge-case handling, and win animations.
# Number Guessing Game 🎯

A simple yet engaging number guessing game built with Streamlit where players try to guess a random number between 1-100 with hot/cold hints.

<img width="1001" height="833" alt="{030AB0DF-CE60-4E27-A5CA-796ACB0F457D}" src="https://github.com/user-attachments/assets/40e11804-49ca-4bf7-9f3c-240a9f42ec36" />

<img width="1034" height="749" alt="{1198DCF6-5AFA-4BD6-B537-3579C48A51B1}" src="https://github.com/user-attachments/assets/fa558606-b77d-4161-9c1b-86bd85b1cf78" />

## Features
- 🔢 Random number generation between 1-100
- ❄️🔥 Hot/Cold hints (within 10 = hot, beyond 10 = cold)
- 🎉 Visual celebration when correct
- 🔄 Instant restart option
- 📝 Clear game instructions

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Open your browser to the local URL provided

## Game Rules
- Guess the secret number between 1-100
- Get "Hot" if within ±10 of the number
- Get "Cold" if more than 10 away
- Win instantly when you guess exactly!

Developed with ❤️ using Python and Streamlit
