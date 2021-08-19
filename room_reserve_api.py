###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################

###############################################################################
# Class Room_Reserve_API
# The Room_Reserve_API class is designed to store room reservation data

#  Inputs:
#   None
###############################################################################
class Room_Reserve_API:
    def __init__(self):
        self.rooms_reserved = set()

    #####################################################
    # reserve:
    #   function to reserve a hotel room
    #
    # Algorithm:
    #  Use a set (hashmap) to store rooms that have previously
    #  been reserved. Use set over dictionary because the key
    #  is not associated with a value other than already
    #  existing in the hashmap. Set is advantageous because
    #  of its constant lookup and insertion time
    #
    # Time Complexity: O(1)
    #
    # Inputs:
    #   room_to_reserve: string (case insensitive)
    #                    containing the hotel and room
    #                    number requested to be reserved.
    #                    Accuracy of input string is the
    #                    responsibility of the caller.
    #                    The only input checked is an empty string
    #
    # Outputs:
    #   True if room_to_reserve has NOT already been reserved
    #   False if room_to_reserve has already been reserved or is empty string
    #####################################################
    def reserve(self, room_to_reserve):

        # convert all alphabetical characters in input string to make case insensitive
        room_to_reserve = room_to_reserve.lower()

        # return False if empty string or room has already been reserved
        if not room_to_reserve or room_to_reserve in self.rooms_reserved:
            return False

        # otherwise, add hotel room to set that stores the rooms that have been reserved and return True
        else:
            self.rooms_reserved.add(room_to_reserve)
            return True