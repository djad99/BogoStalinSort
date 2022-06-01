# BogoStalin Sort

This sorting algorithm was inspired by Stalin Sort, with a Bogosort twist. In
the spirit of communism, everyone is equal. So therefore everyone is equally
likely to be punished for the mistakes of an individual, as it is society's
fault, not the individual.

Here's the basic algorithm:

Go through every element in the list, and if there is an element (person) out
of place, delete a random element in the list (send a random person to the
gulag). Repeat this process until the list is sorted.

The way implemented in the BogoStalinSort.py file restarts from the beginning
every time an element is deleted, however this is unneccesary. In the mind of
the programmer, this is just a proof of concept for an even less efficient
version of Stalin Sort.

There are variations of this which the programmer has thought of and would like
to document here, and leave as an exercise to the reader, as they would not be
hard to implement

## BogoStalin Sort Less

Instead of deleting a purely random element, delete a random element from the
current position to the end of the list. This should be slightly more efficient,
though again, this is not a practical sort.

## StalinBogo Sort

This is a Stalin Sort twist on BogoSort.
Instead of deleting a random element when stalin sort fails, you delete the
first element out of place in a bogosort, then execute a bogosort again.

This should make Bogosort take significantly less time (Probably polynomial), of
course now there will be significant data loss in every step.

## Closing thoughts

If you have a good grasp of Stalin and Bogo Sort, then it shouldn't be too hard
to create other variations, just figured this is an interesting mark on
inefficient sorting, combing the slowness of bogosort with the data deletion of
Stalin Sort. Have a nice day!
