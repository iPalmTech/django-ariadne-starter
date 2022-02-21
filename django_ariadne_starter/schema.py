from ariadne import gql, make_executable_schema

from school.schema import type_defs as school_types
from school.resolvers import school_query, school_mutation

type_defs= gql("""
type Query{
    all_schools: [School]
    school(schoolId: ID!): School
    
}
type Mutation{
    add_school(input: SchoolInput!): SchoolResults
}
""")

schema = make_executable_schema([school_types, type_defs], school_query, school_mutation)