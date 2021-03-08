
def global_variables(request):
    """
      The context processor must return a dictionary.
    """
    return {
        'domain_name': 'Real-Lex',
        'domain': "https://real-estate.tornode.org",
    }
