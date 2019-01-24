import allure


@allure.step(title="测试登录的流程")
def test_login():
    allure.attach('登录', '输入用户名')
    print('aaaa')
    allure.attach('登录', '输入密码')
    print('bbbb')
    allure.attach('登录', '点击登录')
    print('cccc')
    assert 1
# def test_b():
#     print('bbb')
#     assert 0