from fractions import Fraction


x = 3 / 2
print(Fraction(x))



def fraction_div(x, y):
    div = x/y
    return Fraction(div)

print(fraction_div(3, 2))


"""
> This is less of a Python question than it is an algorithm question, but
> it should still apply since Python has some cool data structures
> available to apply to the solution.

In this case, I think some simple arithmetic will suffice.

> I have a script that does some length calculations and prints out results
> in decimal inches.  (e.g. 1.537", 4.230", etc.)  Converting these to
> fractions of an inch is simple enough (e.g. 1+537/1000, 4+23/100, etc.),
> but suppose I only want answers in the standard fractions of an inch
> (i.e. fourths of and inch, thirty-seconds of an inch, etc.).

The "etc" is important:  how far down do you want to go?  That is, is 1/32
the smallest granularity you care about?

BTW, in my college days, I applied for a job on the Harley-Davidson assembly
line.  I barely made it:  during the interview, the foreman looked me in the
eyes and demanded "how many sixty-fourths of an inch are in an inch?".  It
seemed like *such* a stupid question, I asked him to repeat it.  He did.
Then it seemed like it must be a trick question, and my mind raced futilely
looking for "the trick".  After about a minute, he lost patience and asked
for my answer.  Hesitant and defeated, I weakly asked "umm, 64?".  "Right!"
he beamed, "Now let's see if you can read a micrometer.".
"""

def tofrac(x, largest_denominator=4):
    """Return triple (i, j, k) where x ~= i + j/k.

    x >= 0 is required.
    i, j and k are integers >= 0, and k is > 0.
    j and k have no factors in common, unless j is 0.

    Optional argument largest_denominator (default 32) should be a
    power of 2, and is the largest value k can have.
    """

    if not x >= 0:
        raise ValueError("x must be >= 0")
    scaled = int(round(x * largest_denominator))
    whole, leftover = divmod(scaled, largest_denominator)
    if leftover:
        while leftover % 2 == 0:
            leftover >>= 1
            largest_denominator >>= 1
    return whole, leftover, largest_denominator

formato = "%d %d/%d"
print(formato % tofrac(1.537))
print(formato % tofrac(4.230))
print(formato % tofrac(4.230, 128))
print(formato % tofrac(4.240))
print(formato % tofrac(8))

"""
> I'm looking for suggestions on implementation.  My approach is to use a
> lookup table, probably in dictionary form.  The table will contain "bins"
> of fractions in increments of 1/32 with upper and lower limits for the
> decimal equivlent.  The limits would be calculated by adding and
> subtracting 1/64 to the base number.  For instance, a given decimal
> would be determined to be 3/32 if the decimal equivalent was between
> 0.09375+0.015625 and 0.09375-0.015625.

The code above gets the same effect, pretty much by answering the question
"How many 32nds of an inch are in an inch?" <wink>:  multiply by 32, round
to an int, then take the quotient and remainder from dividing by 32.
"""