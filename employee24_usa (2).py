# Sintaxe:
# from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2, NomeClasse3
from employee24 import Employee, FulltimeEmployee, HourlyEmployee
if __name__ == '__main__':
    # obj_employee = Employee('Emily', 'Pereira')       # TypeError:
    # Can't instantiate abstract class Employee with abstract method compute_salary
    obj_fulltime1 = FulltimeEmployee('John', 'Doe', 6000.0) # Três argumentos
    print('- Fulltime Employee 1:', obj_fulltime1)
    print('Nome:', obj_fulltime1.get_first_name())
    print('Nome completo:', obj_fulltime1.full_name())
    print('Salário fixo:', obj_fulltime1.get_base_salary())
    print('Salário total:', obj_fulltime1.compute_salary())
    obj_fulltime2 = FulltimeEmployee('Rogério', 'Santos') # Dois argumentos
    print('\n- Fulltime Employee 2:\nNome completo:', obj_fulltime2.full_name())

    obj_hourly1 = HourlyEmployee('Vinícius', 'Alves', 20, 200.0) # 4
    print('\n- Hourly Employee 1:', obj_hourly1)
    print('Nome:', obj_hourly1.get_first_name())
    print('Nome completo:', obj_hourly1.full_name())
    print('Valor da hora:', obj_hourly1.get_hour_value())
    print('Salário total:', obj_hourly1.compute_salary())
    obj_hourly2 = HourlyEmployee('Emily', 'Duarte', 20) # Três argumentos
    print('\n- Hourly Employee 2:\nNome completo:', obj_hourly2.full_name())

    # print("Funcionários cadastrados:", Employee.count_employees())
