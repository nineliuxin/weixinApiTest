import pystache


class Utils:
    @classmethod
    def parse(cls, template_path, dict):
        template = "".join(open(template_path).readlines())
        return pystache.render(template, dict)