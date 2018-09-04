from cgi import parse_qs

def app(environ, start_response):   
    start_response("200 OK", [("Content-Type", "text/plain")])
    #qs = parse_qs(environ['QUERY_STRING'])
    return iter([b"\n".join(environ.get('QUERY_STRING').split("&"))])
    #return['%s=%s\n' % (k, qs[k][0]) for k in qs]
