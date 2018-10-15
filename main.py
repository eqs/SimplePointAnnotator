# -*- coding: utf-8 -*-
"""
Created on 10/15/18 22:40:39

Flask

@author: eqs
"""

from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

projects = {}

class ProjectResource(Resource):
    def post(self, project_id):
        """プロジェクトを新しく作る
        :param project_id: プロジェクトの識別子
        """

        if project_id in projects.keys():
            abort(401, message=f'"{project_id}" is already exists.')
        
        projects[project_id] = {
            'project path': f'{project_id}.json', 
            'images': []
        }

        return projects[project_id], 200

    def put(self, project_id):
        """プロジェクトをファイルに書き出す
        :param project_id: プロジェクトの識別子
        """
        if not project_id in projects.keys():
            abort(404, message=f'"{project_id}" is not found.')

        # TODO: プロジェクトをファイルに書き出す

        return projects[project_id], 200

    def get(self, project_id):
        """プロジェクトを取得する
        :param project_id: プロジェクトの識別子
        """
        
        if not project_id in projects.keys():
            abort(404, message=f'"{project_id}" is not found.')

        return projects[project_id], 200

    def delete(self, project_id):
        """プロジェクトを消す
        :param project_id: プロジェクトの識別子
        """
        
        if not project_id in projects.keys():
            abort(404, message=f'"{project_id}" is not found.')

        del projects[project_id]

        return '', 200

api.add_resource(ProjectResource, '/<string:project_id>')

if __name__ == '__main__':
    app.run(debug=True)
