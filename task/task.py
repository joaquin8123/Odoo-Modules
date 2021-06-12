# -*- coding: utf-8 -*- 
from odoo import models, fields 
class TodoTask(models.Model): 
    _name = 'task.task' 
    _description = 'Task'


    #campos
    name = fields.Char('Nombre', required=True)
    state = fields.Selection([ ('draft', 'Borrador'),('progress','En Curso'),('done','Finalizado'),('cancel','Cancelado')],'Estado', default='draft')
    description = fields.Text('Descripcion')
    is_done = fields.Boolean('Done')
    technologies_ids = fields.Many2many('task.technology','task_task_technology_rel' ,'task_id','technology_id', 'Tecnologias') 
    active = fields.Boolean('Active', default=True)
    
    def btn_progress(self):
        for obj in self:
            if obj.state == 'draft' and obj.name and obj.technologies_ids:
                obj.state = 'progress'
        return True
    
    def btn_cancelar(self):
        for obj in self:
            if obj.state == 'draft' or obj.state == 'progress':
                obj.state = 'cancel'
        return True

    

class TaskTechnology(models.Model): 
    _name = 'task.technology' 
    _description = 'Task Technology'


    #campos
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripcion')
    active = fields.Boolean('Active', default=True)