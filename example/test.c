#define WAPHICS_IMPLEMENTATION
#include "../src/waphics.c"

#define WIDTH 1000
#define HEIGHT 600

uint32_t pixels[WIDTH * HEIGHT];
Surface display;

void init(void) {
    display = SURFACE(pixels, WIDTH, HEIGHT);
}

int x;

uint32_t *render(void) {
    // fill the display with black
    waphics_fill_display(display, RGB(0, 0, 0));
    // draw a red rectangle
    waphics_draw_rect(display, RECT(x, 0, 50, 50), RGB(255, 0, 0));
    // draw a blue circle
    waphics_draw_circle(display, CIRCLE(x, 120, 50), RGB(0, 100, 100));

    if (get_key(KEY_D)) x+=10;
    if (get_key(KEY_A)) x-=10;

    return display.pixels;
}