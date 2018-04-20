import math


def custompaginator(num_pages, current_page, max_page):
    middle = math.ceil(max_page / 2)
    # ������������ҳ��С�������ʾ��ҳ��
    if num_pages < max_page:
        start = 1
        end = num_pages
    else:
        # ��ǰҳС�ڵ���middle ʱ��
        if current_page <= middle:
            start = 1
            end = max_page
        else:
            # �м����
            start = current_page - middle
            end = current_page + middle - 1
            # ��ǰҳ��β�͵����
            if current_page + middle > num_pages:
                start = num_pages - max_page + 1
                end = num_pages
    return start, end
