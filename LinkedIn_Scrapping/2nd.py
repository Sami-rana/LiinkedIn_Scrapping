from itertools import combinations

# Dictionary of people and their skills
people_skills = {
    'A': {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'},
    'B': {'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k'},
    'C': {'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'},
    'D': {'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'},
    'E': {'n', 'o', 'p', 'q', 'r', 's', 't', 'u'},
    'F': {'a', 'b', 'c', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    'G': {'a', 'e', 'i', 'o', 'u', 'y'},
    'H': {'b', 'c', 'e', 'g', 'k', 'm', 'q', 's', 'x'}
}
# {'a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't'}
# Function to generate project groups
def generate_project_groups(necessary_skills):
    project_groups = []
    for group_size in range(1, len(people_skills) + 1):
        for group in combinations(people_skills.keys(), group_size):
            group_skills = set().union(*(people_skills[person] for person in group))
            if group_skills.issuperset(necessary_skills):
                project_groups.append(group)
    return project_groups

# Function to print project groups
def print_project_groups(groups):
    for group in groups:
        print(' '.join(group))

# Main function
if __name__ == "__main__":
    necessary_skills = {'a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't'}
    groups = generate_project_groups(necessary_skills)
    print_project_groups(groups)
# from itertools import combinations
#
# # Dictionary of people and their skills
# people_skills = {
#     'A': 'abcdefgh',
#     'B': 'defghijk',
#     'C': 'ghijklmn',
#     'D': 'klmnopqr',
#     'E': 'nopqrstu',
#     'F': 'rstuvwxyz',
#     'G': 'aeiouy',
#     'H': 'bcegkmqsx'
# }
#
#
# # Function
# # to generate all possible project groups
# def generate_project_groups(necessary_skills):
#     project_groups = []
#     for i in range(1, len(people_skills) + 1):
#         for group in combinations(people_skills.keys(), i):
#             group_skills = set()
#             for person in group:
#                 group_skills.update(people_skills[person])
#             if group_skills.issuperset(set(necessary_skills)):
#                 project_groups.append(group)
#     return project_groups
#
#
# # Function to format and print project groups
# def print_project_groups(groups):
#     for group in groups:
#         group_names = ' '.join(group)
#         print(group_names)
#
#
# # Main function
# def main():
#     # Example inputs
#     example_inputs = [
#         ['l', 'q', 's'],
#         ['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']
#     ]
#
#     for input_skills in example_inputs:
#         print("Input:", ' '.join(input_skills))
#         project_groups = generate_project_groups(input_skills)
#         print("Output:")
#         print_project_groups(project_groups[:5])  # Limiting output to 5 groups
#         print()
#
#
# if __name__ == "__main__":
#     main()
#
# from itertools import combinations
#
#
# # Dictionary of people and their skills
# people_skills = {
#     'A': 'abcdefgh',
#     'B': 'defghijk',
#     'C': 'ghijklmn',
#     'D': 'klmnopqr',
#     'E': 'nopqrstu',
#     'F': 'rstuvwxyz',
#     'G': 'aeiouy',
#     'H': 'bcegkmqsx'
# }
#
#
# # Function to generate all possible project groups
# def generate_project_groups(necessary_skills):
#     project_groups = []
#     for i in range(1, len(people_skills) + 1):
#         for group in combinations(people_skills.keys(), i):
#             group_skills = set()
#             group_names = []
#             for person in group:
#                 group_skills.update(people_skills[person])
#                 group_names.append(person)
#             if group_skills.issuperset(set(necessary_skills)):
#                 project_groups.append(group)
#     return project_groups
#
#
# # Function to format and print project groups
# def print_project_groups(groups):
#     for group in groups:
#         group_names = ' '.join(group)
#         print(group_names)
#
#
# # Main function
# def main():
#     # Example inputs
#     example_inputs = [
#         ['l', 'q', 's'],
#     ]
#
#     for input_skills in example_inputs:
#         print("Input:", ' '.join(input_skills))
#         project_groups = generate_project_groups(input_skills)
#         print("Output:")
#         print_project_groups(project_groups[:5])  # Limiting output to 5 groups
#         print()
#
#
# if __name__ == "__main__":
#     main()
