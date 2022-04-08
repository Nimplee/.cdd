#ifndef UNICODE
#define UNICODE
#endif

#include "Window.h"

Window window;

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow) {
	window.Initialize(hInstance, hPrevInstance, pCmdLine, nCmdShow);

	return 0;
}