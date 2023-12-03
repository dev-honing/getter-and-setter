# Docstring.py

# DocString 표기 스타일 - Sphinx 스타일 / Google 스타일
# Sphinx 스타일
def test(usage):
    """
    테스트 함수

    Parameters:
    usage : str
        사용법에 대한 설명 문자열
    """
    print('테스트')
    print(f'사용법: {usage}')

# Google 스타일
def test(usage):
    """
    테스트 함수

    Args:
        usage (str): 사용법에 대한 설명 문자열
    """
    print('테스트')
    print(f'사용법: {usage}')

# test 함수 호출 시 매개변수 전달
test(usage='이 함수는 테스트용임.')
