from django import template

register = template.Library()


@register.filter(name="total")
def total(item):
    return item.quantity *  item.product.price


@register.filter(name="grand_total")
def grand_total(cart):
    g_total =0
    for item in cart:
        g_total += item.quantity *  item.product.price
    return g_total