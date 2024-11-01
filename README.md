
This program is a Telegram bot designed to solve quadratic equations and return the result as an image. Here’s a breakdown of how it works:

![Screenshot](https://github.com/PoweRFullGG/Math_Helper/blob/main/Screenshot_238.png)

User Interface: The bot greets the user with buttons for "Quadratic Equation Solution" and "About the Bot." When the user selects the equation option, they are prompted to enter the coefficients (a, b, c) in a single line.

Equation Solving: Based on the entered coefficients, the bot calculates the discriminant and then finds the roots of the equation if possible.

If the discriminant is negative, the bot informs the user that there are no real roots.

If it’s zero, it returns the single root.

If positive, it calculates both roots.

Image Generation: For equations with real roots, the bot generates an image showing the solution step-by-step using the Python Imaging Library (PIL). This image is sent back to the user as a photo.

User-Friendly: After solving, the bot returns to the main menu, allowing the user to try again or learn more about the bot.

This bot is convenient for quickly solving quadratic equations with a visual solution in Telegram.
