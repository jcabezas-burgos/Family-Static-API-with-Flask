
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]},
            {
            "id": 2,
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]},
            {
            "id": 3,
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]},
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member ['id'] = self._generateId()
        if ('first_name' in member and 'age' in member and 'lucky_numbers' in member):
            self._members.append(member)
            return "member added successfully"
        else:
            return "error adding new member"

    def delete_member(self, id):
        # fill this method and update the return
        for idx, member in enumerate(self._members):
            if id == member['id']:
                self._members.pop(idx)
                return {"done": True}
        return "member not found"

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if id == member['id']:
                return member
        return "member not found"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
