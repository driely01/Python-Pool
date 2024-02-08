from find_ft_type import all_things_is_obj

ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Morocco")
ft_set = {"Hello", "Khouribga"}
ft_dict = {"Hellp" : "1337"}

all_things_is_obj(ft_list)
all_things_is_obj(ft_tuple)
all_things_is_obj(ft_set)
all_things_is_obj(ft_dict)
all_things_is_obj("Brain")
all_things_is_obj("Toto")
print(all_things_is_obj(10))