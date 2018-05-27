Title: Primtal
Date: 2018-05-23
Modified: 2018-05-23
Category: Matematik
Tags: Ma1; Python
Slug: primtal
Author: Stefan Sollander
Summary: En introducerande artikel till primtal.

## Primtal ##

Primtal är en av de fundamentala byggstenarna inom de område som heter talteori i Matematiken. Egenskapern har i och med introduktionen av datorerna från sent 1900-tal och framåt fått ett rejält uppsving. Primtalen används i allt från prestandatestning till kanske den viktigaste tilläpningen där de används till kryptering mellan sändare och mottagare på internet.

Men låt oss börja med en defintion.

	Primtal är ett positivt heltal som endast är delbart med sig själv och talet ett.

Test om ett tal är ett heltal eller inte.

	def PrimtalsTest(n):
		for i in range(n/2):
			if (n & i == 0):
				return false

Slut på artikeln.

//[SoS]({author}Stefan Sollander)

[Startsidan]({index}Startsidan)

