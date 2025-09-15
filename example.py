from ssiaquitaine.tasks import TaskManager

tm = TaskManager()
tm.add_task("Analyser logs firewall", "Audit sécurité hebdomadaire", "high")
tm.add_task("Former équipe", "Session de sensibilisation SSI", "medium")
tm.update_status(1, "in-progress")
tm.list_tasks()
tm.export_report()
