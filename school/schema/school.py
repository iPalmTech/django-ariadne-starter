from ariadne import gql



type_defs = gql( """

    type School {
        id: ID
        school_name: String!
        school_population: Int!
        added_on: String!
    }

    input SchoolInput {
        school_name: String
        school_population: Int
        added_on: String
    }

    type SchoolResults {
        created: Boolean!
        school: School
        err: String
    }
""")