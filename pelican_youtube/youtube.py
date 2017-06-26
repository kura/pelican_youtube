# -*- coding: utf-8 -*-

# Copyright (c) 2013 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class YouTube(Directive):
    """ Embed YouTube video in posts.

    Based on the YouTube directive by Brian Hsu:
    https://gist.github.com/1422773

<<<<<<< HEAD
    VIDEO_ID is required, other arguments are optional

    Usage:
    .. youtube:: VIDEO_ID
=======
    VIDEO_ID is required, with / height are optional integer,

    Usage:
    .. youtube:: VIDEO_ID
        :width: 640
        :height: 480
>>>>>>> d34a1ac35df85cdc779ad8add1b2c316d1ddbfaf
    """

    def boolean(argument):
        """Conversion function for yes/no True/False."""
        value = directives.choice(argument, ('yes', 'True', 'no', 'False'))
        return value in ('yes', 'True')

    def yesno(argument):
        return directives.choice(argument, ('yes', 'no'))

    required_arguments = 1
    optional_arguments = 5
    option_spec = {
        'class': directives.unchanged,
        'width': directives.positive_int,
        'height': directives.positive_int,
<<<<<<< HEAD
        'allowfullscreen': boolean,
        'seamless': boolean,
=======
        'align': align, # back compatibility
        'nocookie': yesno,
>>>>>>> d34a1ac35df85cdc779ad8add1b2c316d1ddbfaf
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        videoID = self.arguments[0].strip()
<<<<<<< HEAD
        url = 'https://www.youtube.com/embed/{}'.format(videoID)
=======
        width = 420
        height = 315
        domain = 'www.youtube.com'
>>>>>>> d34a1ac35df85cdc779ad8add1b2c316d1ddbfaf

        width = self.options['width'] if 'width' in self.options else None
        height = self.options['height'] if 'height' in self.options else None
        fullscreen = self.options['allowfullscreen'] \
            if 'allowfullscreen' in self.options else True
        seamless = self.options['seamless'] \
            if 'seamless' in self.options else True

        css_classes = 'youtube'
        if 'class' in self.options:
            css_classes += ' {}'.format(self.options['class'])
        elif height is None:
            # use responsive design with 16:9 aspect ratio by default
            css_classes += ' {}'.format('youtube-16x9')
        # no additional classes if dimensions (height/width) are specified

<<<<<<< HEAD
        iframe_arguments = [
            (width, 'width="{}"'),
            (height, 'height="{}"'),
            (fullscreen, 'allowfullscreen'),
            (seamless, 'seamless frameBorder="0"'),
        ]

        div_block = '<div class="{}">'.format(css_classes)
        embed_block = '<iframe src="{}" '.format(url)

        for value, format in iframe_arguments:
            embed_block += (format + ' ').format(value) if value else ''

        embed_block = embed_block[:-1] + '></iframe>'
=======
        if 'nocookie' in self.options and self.options['nocookie'] == 'yes':
            domain = 'www.youtube-nocookie.com'


        url = 'https://{}/embed/{}'.format(domain, videoID)
        div_block = '<div class="youtube">'
        embed_block = '<iframe width="{}" height="{}" src="{}">'\
                      '</iframe>'.format(width, height, url)
>>>>>>> d34a1ac35df85cdc779ad8add1b2c316d1ddbfaf

        return [
            nodes.raw('', div_block, format='html'),
            nodes.raw('', embed_block, format='html'),
            nodes.raw('', '</div>', format='html'),
        ]


def register():
    directives.register_directive('youtube', YouTube)
