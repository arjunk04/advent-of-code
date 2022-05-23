# Part One

Start at depth and horizontal position of 0

Input has multiple lines, each of which is formatted like so: 
[forward/up/down] X

- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.


After following everything, multipy the horizontal and vertical position by two

# Part Two

Keep track of an additional measure aim, such that:
- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
	- It increases your horizontal position by X units.
	- It increases your depth by your aim multiplied by X.

