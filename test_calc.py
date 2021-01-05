import pytest
import yaml
from calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始")

    def teardown_class(self):
        print("结束")

    def get_datas():
        with open("./data.yml") as f:
            data = yaml.safe_load(f)
            print(data)
            add_data = data["add_data"]
            add_id = data["add_id"]
            sub_data = data["sub_data"]
            sub_id = data["sub_id"]
            mul_data = data["mul_data"]
            mul_id = data["mul_id"]
            def_data = data["def_data"]
            def_id = data["def_id"]
            return [add_data, add_id, sub_data, sub_id, mul_data, mul_id, def_data, def_id]


    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[0],
                             ids=get_datas()[1])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[2],
                             ids=get_datas()[3])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[4],
                             ids=get_datas()[5])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[6],
                             ids=get_datas()[7])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
