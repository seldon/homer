from django import template
from simplyblock.models import Content

register = template.Library()

class BlockContentNode(template.Node):
    def __init__(self, block_name,action='get'):
        self.block_name = block_name
        self.action = action
    def render(self,context):
        block_content = Content.objects.get(block_name = self.block_name)
        if self.action == 'make':
            div = "<div class='%s-wrapper simplyblock' ><div class='%s'><div class='title'>%s</div><div class=content>%s</div></div>" % (block_content.block_name, 
                                                                                                                                   block_content.block_name,
                                                                                                                                   block_content.title,
                                                                                                                                   block_content.body)
            return div
        elif self.action == 'get':
            context[self.block_name] = block_content
            return ''            



def get_block_content(parser,token):
    bits = token.split_contents()
    if len(bits) == 2:
        return BlockContentNode(bits[1], )
    elif len(bits) == 3:
        return BlockContentNode(bits[1], bits[2])
    else:
        raise template.TemplateSyntaxError("'get_block_content' tag 1 or 2 arguments")



register.tag('block_content', get_block_content)

