from .types import Record

def process_record_message(text: str) -> Record:
    '''do something with records'''
    
    category, name, ammount, *comments = text.split(' ')

    comment = ''.join(comments)

    return Record(
        category=category,
        name=name,
        ammount=ammount,
        comment=comment,
    )
