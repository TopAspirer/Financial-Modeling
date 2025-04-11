Written April 11, 2025

Hi, How's it going!

I'm really happy that you've got here, that means I made something thats worth someones time to take more of a look into.
Consider sending me a message if you'd like to know more or talk about something: tendolloyd@gmail.com

The majority of this tool operates on the basis of a few simple formulas I derived one line and understood abit more in my math and accounting classes.

Calculating the salary:
S_t = S_o (1+ r_i)**t (1+r_p)**p

- S_t: salary at year t
- S_o: starting salary
- r_i: annual salary raise (%)
- r_p: promotion raise (%)
- t: number of years
- p: number of promotion

This is the base formula as of the first version. It's being added onto and the current is much more elaborate than this.


Calculating Wealth:
This formula in the tool was broken up into cash saved and wealth mainly to see how the cash saved is accumulated over time vs the wealth accumulated over time.

W_t - W_o(1+r_i)**t +S_t*V

- W_t: wealth at year t
- W_o: beginning/current wealth
- r_i: investment return rate (%)
- S_t: salary at that year
- t: number of years
- V: savings rate (%)

How is the year of retirment year determined?
The wealth calculation is run in while loop until the defined desired income has been met or surpassed.

  


