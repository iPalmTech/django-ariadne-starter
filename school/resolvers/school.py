from ariadne import MutationType, QueryType
from ..models import School

school_query = QueryType()

@school_query.field("all_schools")
def resolve_all_schools(*_):
    return School.objects.all()

@school_query.field("school")
def resolve_school(*_, schoolId):
    school = School.objects.get(pk=schoolId)
    if school: return school 
    else: return None

school_mutation = MutationType()

@school_mutation.field('add_school')
def resolve_add_school(_, info, input):
    school = School.objects.create(school_name=input['school_name'], school_population=input['school_population'], added_on=input['added_on'])
    school.save()

    return {'created': True, 'school': school, 'err': ''}