from itertools import combinations

# Dictionary of people and their skills
people_skills = {
    "A": {"a", "b", "c", "d", "e", "f", "g", "h"},  # Albert
    "B": {"d", "e", "f", "g", "h", "i", "j", "k"},  # Balder
    "C": {"g", "h", "i", "j", "k", "l", "m", "n"},  # Carla
    "D": {"k", "l", "m", "n", "o", "p", "q", "r"},  # Dorte
    "E": {"n", "o", "p", "q", "r", "s", "t", "u"},  # Eric
    "F": {"a", "b", "r", "s", "t", "u", "v", "w", "x", "y", "z"},  # Finn
    "G": {"a", "e", "i", "o", "u", "y"},  # Gurli
    "H": {"b", "c", "e", "g", "k", "m", "q", "s", "x"},  # Hugo
}


def generate_project_groups(necessary_skills):
    """
    Generates project groups based on the necessary skills.

    Args:
        necessary_skills (list): List of necessary skills for the project.

    Returns:
        list: List of tuples representing project groups.
    """
    project_groups = []
    for i in range(1, len(people_skills) + 1):
        for group in combinations(people_skills.keys(), i):
            group_skills = set()
            for person in group:
                group_skills.update(people_skills[person])
            if group_skills.issuperset(set(necessary_skills)):
                project_groups.append(group)
    return project_groups


def print_project_groups(groups):
    """
    Prints the project groups.

    Args:
        groups (list): List of tuples representing project groups.
    """
    for group in groups:
        print(' '.join(group))


def main():
    """
    Main function to demonstrate the generation of project groups.
    """
    example_inputs = [
        ['l', 'q', 's'],
        ['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']
    ]

    for input_skills in example_inputs:
        print("Input:", ' '.join(input_skills))
        project_groups = generate_project_groups(input_skills)
        print("Output:")
        print_project_groups(project_groups)
        print()


if __name__ == "__main__":
    main()
