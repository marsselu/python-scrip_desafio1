##### certamente falta algo, mas foi o que consegui desenvolver ate agora. Obrigado !

# utilizando o pyCharm, foi instalado o package 'Crontab'
#importando biblioteca (usuario deve ter permissao de 'superuser')
from crontab import CronTab

empty_cron    = CronTab()
my_user_cron  = CronTab(user=True)
users_cron    = CronTab(user='username')


#criando um novo job
job = cron.new(command='/usr/bin/echo')

#setando os 'times' dos jobs
job.minute.during(5,50).every(5)
job.hour.every(4)
job.day.on(4, 5, 6)
job.dow.on('SUN')
job.dow.on('SUN', 'FRI')
job.month.during('APR', 'NOV')
job.every(4).hours()  == '0 */4 * * *'
job.every().dom()     == '0 0 * * *'
job.every().month()   == '0 0 0 * *'
job.every(2).dows()   == '0 0 * * */2'

#setando todos de uma vez
job.setall(2, 10, '2-4', '*/2', None)
job.setall('2 10 * * *')

#setando para um objeto python
job.setall(time(10, 2))
job.setall(date(2000, 4, 2))
job.setall(datetime(2000, 4, 2, 10, 2))

#rodando comando de job
job_standard_output = job.run()
