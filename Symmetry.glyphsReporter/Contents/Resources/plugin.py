# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class Symmetry(ReporterPlugin):

	def settings(self):
		self.hFlip = True
		self.vFlip = True
		
		self.menuName = Glyphs.localize({
			'en': u'Symmetry',
			'de': u'Symmetrie',
			'fr': u'Symmetrie'
		})
		self.generalContextMenus = [
		{
			'name': Glyphs.localize({
				'en': u'Toggle Horizontal Flip',
				'de': u'Schalte horizontale Spiegelung um'}),
			'action': self.toggleHFlip
		},
		{
			'name': Glyphs.localize({
				'en': u'Toggle Vertical Flip',
				'de': u'Schalte vertikale Spiegelung um'}),
			'action': self.toggleVFlip
		},
		]
		
	def background(self, Layer):
		hScale, vScale = 1.0, 1.0
		xShift, yShift = 0.0, 0.0
		if self.hFlip:
			hScale = -1.0
			xShift = Layer.bounds.origin.x * 2 + Layer.bounds.size.width
		if self.vFlip:
			vScale = -1.0
			yShift = Layer.bounds.origin.y * 2 + Layer.bounds.size.height

		NSColor.colorWithCalibratedRed_green_blue_alpha_( 1.0, 1.0, 0.0, 0.4 ).set()
		bezierPath = Layer.bezierPath
		mirroring = NSAffineTransform.transform()
		mirroring.scaleXBy_yBy_( hScale, vScale )
		mirroring.translateXBy_yBy_( -xShift, -yShift )
		mirroredImage = mirroring.transformBezierPath_( bezierPath )
		mirroredImage.fill()
	
	def toggleHFlip(self):
		self.hFlip = not self.hFlip
		
	def toggleVFlip(self):
		self.vFlip = not self.vFlip
		

