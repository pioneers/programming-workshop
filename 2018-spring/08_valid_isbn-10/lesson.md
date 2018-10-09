# Valid ISBN-10

    def valid_isbn_ten(num):

In 1970, the International Organization for Standardization (ISO) published a standard describing how every publicly published book ought to be issued a specially constructed number. Among other things, each International Standard Book Number (ISBN) provides a way to uniquely identify books, since not every book has a unique title, author, or publisher. 

These ISBNs are especially useful for building digital catalogues. This is because as it is generally much easier for computers to search a large database for a very specific ISBN than for a provided title that could have multiple variations, capitalization differences, or even typos to account for!

However, trying to manage these numbers by hand is very error-prone: if an ISBN is off by a single digit, then it could refer to a completely different book, or none at all! To protect against human error, the designers of ISBN-10 included a simple scheme for checking if an ISBN-10 is invalid: we apply a certain math function onto the left-most 9 digits of the ISBN-10 and see the output is the same as the right-most digit. If it isn’t, then we know that this ISBN-10 is invalid!†

Your task is to check that the input is a valid ISBN-10 number. If the input is a valid ISBN-10 number, then just return the input. Otherwise, return the next smallest integer that is valid.

An ISBN-10 number’s validity is checked as follows:

* There is a special sum (of 10 numbers) that needs to be calculated—this is called a check-digit.
* Each one of these numbers is the position of the digit multiplied by the digit at that position.
  * For example, the checksum of 0-306-40615-2 is calculated as follows:
  * (10 * 0) + (9 * 3) + (8 * 0) + (7 * 6) + (6 * 4) + (5 * 0) + (4 * 6) + (3 * 1) + (2 * 5) + (1 * 2).
* The ISBN-10 number is valid if the check-digit is divisible by 11.

Examples:

    >>> valid_isbn_ten(2)
    19
    >>> valid_isbn_ten(3)
    19
    >>> valid_isbn_ten(128122765)
    128122765
    >>> valid_isbn_ten(128122760)
    128122765
    >>> valid_isbn_ten(60)
    78
    >>> valid_isbn_ten(123456788)
    123456789

†More generally, this idea is known as a checksum. It’s used in credit card numbers, vehicle identification numbers (VIN), and in most barcodes found in stores (UPC).
