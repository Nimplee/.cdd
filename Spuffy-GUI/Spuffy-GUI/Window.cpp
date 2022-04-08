#include "Window.h"

bool Window::Initialize(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow)
{
    const wchar_t CLASS_NAME[] = L"Spuffy";
    
    WNDCLASS wc = { };
    wc.lpfnWndProc = WindowProc;
    wc.lpszClassName = CLASS_NAME;
    wc.hInstance = hInstance;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        NULL,
        CLASS_NAME, L"Spuffy GUI",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 1200, 800,

        NULL, NULL, hInstance, NULL
    );

    if (hwnd == NULL)
        return false;

    ShowWindow(hwnd, nCmdShow);

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return true;
}

LRESULT CALLBACK Window::WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
    case WM_CLOSE:
        if (MessageBox(hwnd, L"Are you sure you want to close Spuffy?", L"Sure?", MB_OKCANCEL) == IDOK)
            DestroyWindow(hwnd);
        return 0;
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    DefWindowProc(hwnd, uMsg, wParam, lParam);
}
