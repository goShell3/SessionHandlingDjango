class Person():
    def __init__(self, request):
        self.session = request.session

        person = self.session.get('session_key')

        if 'session_key' not in request.session:
            person = self.session['session_key'] = { }

        self.person = person