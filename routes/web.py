from flask import jsonify, Response, request, Blueprint, render_template, redirect, url_for
from src.base.base import db


bp = Blueprint('web',  __name__)


@bp.route('/', methods=['GET'])
def index():
	return 'OK'

@bp.route('/contato', methods=['GET'])
def contato():
	return render_template('contato.html')

@bp.route('/contato-receive', methods=['POST'])
def recv_contact():
	data = request.form.to_dict()
	db.engine.execute(f"INSERT INTO `test`.`contact`(`name`,`email`,`mensagem`,`telefone`) VALUES(\'{data['name']}\', \'{data['email']}\', \'{data['msg']}\', \'{data['telefone']}\')")
	return 'RECEBI!'
