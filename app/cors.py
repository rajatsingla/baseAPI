from hug.middleware import CORSMiddleware


class CORSMine(CORSMiddleware):
    def process_response(self, request, response, resource, req_succeeded):
        super().process_response(request, response, resource, req_succeeded)
        if request.method == "OPTIONS":
            allowed_methods = response.get_header("Access-Control-Allow-Methods")
            allowed_methods = str(allowed_methods) + " ,DELETE"
            response.set_header("Access-Control-Allow-Methods", allowed_methods)
            response.set_header("Allow", allowed_methods)
