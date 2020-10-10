class Registration:
    
    @staticmethod
    def register_user(email, password, first_name, last_name):
        if ("@" in email) and (len(password) > 6):
            return Profile(first_name, last_name)


class FbModel:
    def __init__(self, profile_picture, cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture

    def get_profile_picture_url(self):
        return "www.fb.com/" + self.profile_picture

    def get_cover_picture_url(self):
        return "www.fb.com/" + self.cover_picture

class Profile(FbModel):
    
    def __init__(self, first_name, last_name, profile_picture = None, cover_picture = None):
        super().__init__(profile_picture, cover_picture)
        self.first_name = first_name
        self.last_name = last_name
    @property
    def get_full_name(self):
        return self.first_name + " - " + self.last_name

    def __str__(self):
        return self.first_name + " - " + self.last_name + " - " + self.get_profile_picture_url() + self.get_cover_picture_url()

class Page(FbModel):
    def __init__(self, name, profile_picture, cover_picture, followers=0):
        super().__init__(profile_picture, cover_picture)
        self.name = name
        self.followers = followers

    def get_info(self):
        return {
            'name':self.name,
            'followers':self.followers
        }

    def __add__(self, other):
        return self.name + " - " + other.name + " - " + " Total Followers: " + str(self.followers + other.followers)

    def __sub__(self,other):
        return self.name + " - " + other.name + " - " + " Total Followers: " + str(self.followers - other.followers)


'''
user1 = Profile(first_name = "Arman", last_name = "Avetisyan", profile_picture = "arman.jpg", cover_picture = "arman_cover.jpg")
user2 = Profile(first_name = "John", last_name = "Smith", profile_picture = "john.jpg", cover_picture = "john_cover.jpg")


pageOne = Page("Profile Page One", "profile_one.jpg", "cover_one.jpg", 1500)
pageTwo = Page("Profile Page Two", "profile_two.jpg", "cover_two.jpg", 4500)

print(pageTwo - pageOne)
'''

myProfile = Registration.register_user("sargis@gmail.com", "Password123!", "Sargis", "Grigoryan")
print(myProfile.get_full_name)