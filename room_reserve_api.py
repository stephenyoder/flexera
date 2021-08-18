###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################

###############################################################################
# Class Room_Reserve_API
# The Room_Reserve_API class is designed to store room reservation data

#  Inputs:
#   stock_prices: None
###############################################################################
class Room_Reserve_API:
    def __init__(self):
        self.rooms_reserved = set()

    #####################################################
    # function to reserve a hotel room
    #
    # Algorithm:
    #  Use a set (hashmap) to store rooms that have previously
    #  been reserved. Use set over dictionary because the key
    #  is not associated with a value other than already
    #  existing in the hashmap.
    #
    # Time Complexity: O(1)
    #
    # Inputs:
    #   room_to_reserve: string containing the hotel and room
    #                    number requested to be reserved.
    #                    Accuracy of input string is the
    #                    responsibility of the caller.
    #
    # Outputs:
    #   True if room_to_reserve has NOT already been reserved
    #   False if room_to_reserve has already been reserved or is empty string
    #####################################################
    def reserve(self, room_to_reserve):
        if not room_to_reserve or room_to_reserve in self.rooms_reserved:
            return False
        else:
            self.rooms_reserved.add(room_to_reserve)
            return True