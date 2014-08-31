__author__ = 'proberts'

import optparse

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

from pbr import app


__port = 701


def getPort(value):
    return (__port, value)[value > 0]


def production(option, opt_str, value, parser):
    print 'Running Production on port {port}...'.format(port=getPort(value))

    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)

    reactor.listenTCP(getPort(value), site, interface="0.0.0.0")
    reactor.run()


def development(option, opt_str, value, parser):
    print 'Running Development Server on port {port}...'.format(port=getPort(value))

    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)

    reactor.listenTCP(getPort(value), site, interface="0.0.0.0")
    reactor.run()


def main():
    parser = optparse.OptionParser(usage="%prog [options] or type %prog -h (--help)")
    parser.add_option('--production', help='Production Web Server', action="callback", callback=production, type="int")
    parser.add_option('--development', help='Built in Development Server', action="callback", callback=development,
                      type="int")
    (option, args) = parser.parse_args()
    parser.print_help()


if __name__ == "__main__":
    main()
