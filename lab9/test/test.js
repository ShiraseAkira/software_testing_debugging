const chai = require('chai');
const sinon = require('sinon');
const sinonChai = require('sinon-chai');
const chaiHttp = require('chai-http');

chai.use(sinonChai);
chai.use(chaiHttp);

const expect = chai.expect;
const should = chai.should();
const assert = chai.assert;

const test_data = require('./test-data.json');

const BASE_URL = 'http://shop.qatl.ru/api/';

const LIST_ENDPOINT = 'products';
const ADD_ENDPOINT = 'addproduct';
const EDIT_ENDPOINT = 'editproduct';
const DELETE_ENDPOINT = 'deleteproduct?id=';

describe('API tests', () => {
    let created_ids = [];
    after(() => {
        for (const id of created_ids) {
            chai.request(BASE_URL)
            .get(DELETE_ENDPOINT + id)
            .end((err, res) => {
            });
        }
    });

    describe('Products list test', () => {
        it('Getting products should have non empty list', (done) => {
            chai.request(BASE_URL)
            .get(LIST_ENDPOINT)
            .end((err, res) => {
                res.should.have.status(200);
                res.should.to.be.json;
                res.body.should.be.a('array');
                res.body.length.should.be.above(0);
                done();
            });
        });
        it('Creating a product, list should be longer', (done) => {
            let product_list_length;
            chai.request(BASE_URL)
            .get(LIST_ENDPOINT)
            .end((err, res) => {
                product_list_length = res.body.length;
                chai.request(BASE_URL)
                .post(ADD_ENDPOINT)
                .send(test_data["valid"])
                .end((err, res) => {
                    created_ids.push(res.body.id);
                    chai.request(BASE_URL)
                    .get(LIST_ENDPOINT)
                    .end((err, res) => {
                        res.body.length.should.be.above(product_list_length)
                        done();
                    });
                });
            });
        }).timeout(5000);
    });

    describe('Update product test', () => {
        it('Updating without id should not update', (done) => {
            let old_category_id;
            chai.request(BASE_URL)
            .post(ADD_ENDPOINT)
            .send(test_data["valid"])
            .end((err, res) => {
                created_ids.push(res.body.id);
                chai.request(BASE_URL)
                .get(LIST_ENDPOINT)
                .end((err, res) => { 
                    old_category_id = res.body[res.body.length - 1]["category_id"];
                    chai.request(BASE_URL)
                    .post(EDIT_ENDPOINT)
                    .send(test_data["valid_update"])
                    .end((err, res) => { 
                        chai.request(BASE_URL)
                        .get(LIST_ENDPOINT)
                        .end((err, res) => { 
                            assert.equal(old_category_id,res.body[res.body.length - 1]["category_id"])
                            done();
                        });
                    });
                });
            });            
        }).timeout(5000);
        it('Updating with valid id should update', (done) => {
            let old_category_id;
            chai.request(BASE_URL)
            .post(ADD_ENDPOINT)
            .send(test_data["valid"])
            .end((err, res) => {
                created_ids.push(res.body.id);
                chai.request(BASE_URL)
                .get(LIST_ENDPOINT)
                .end((err, res) => { 
                    old_category_id = res.body[res.body.length - 1]["category_id"];
                    let updating_info = test_data["valid_update"];
                    updating_info["id"] = res.body[res.body.length - 1]["id"];
                    chai.request(BASE_URL)
                    .post(EDIT_ENDPOINT)
                    .send(updating_info)
                    .end((err, res) => { 
                        chai.request(BASE_URL)
                        .get(LIST_ENDPOINT)
                        .end((err, res) => { 
                            assert.notEqual(old_category_id,res.body[res.body.length - 1]["category_id"])
                            done();
                        });
                    });
                });
            });            
        }).timeout(5000);
    });

    describe('Delete product test', () => {
        it('Deleting existing product should work', (done) => {
            chai.request(BASE_URL)
            .post(ADD_ENDPOINT)
            .send(test_data["valid"])
            .end((err, res) => { 
                chai.request(BASE_URL)
                .get(DELETE_ENDPOINT + res.body.id)
                .end((err, res) => {
                    res.body.status.should.be.equal(1);
                    done();
                });
            });
        }).timeout(5000);
    });
})
