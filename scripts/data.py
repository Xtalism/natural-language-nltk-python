data_files = [
    "data/parsed/messages_data1.txt",
    "data/parsed/messages_data2.txt",
    "data/parsed/messages_data3.txt",
    "data/parsed/messages_data4.txt",
    "data/parsed/messages_data5.txt",
]

patterns = {
    "Substations_all": r"(Subestación Afectada:)([^⚡]+)⚡.*(?:IN-|PR-)[a-z0-9A-Z]+[^\n•]*",
    "IN_numbers": r"IN-[a-z0-9A-Z]+[^\n•]*",
    "Substations_only": r"Subestación Afectada:([^⚡]+)⚡.*IN-[a-z0-9A-Z]+[^\n•]*",
    "PR_numbers": r"PR-[a-z0-9A-Z]+[^\n•]*",
}
