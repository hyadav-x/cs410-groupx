import React from "react";
import { Col, Row } from "react-bootstrap";
import Container from "react-bootstrap/esm/Container";
import Table from "react-bootstrap/Table"
import { Badge } from "react-bootstrap";
import { Image } from "react-bootstrap";
import { Card } from "react-bootstrap";
import CardHeader from "react-bootstrap/esm/CardHeader";
import {HandThumbsUpFill} from  'react-bootstrap-icons';
import {HandThumbsDownFill} from  'react-bootstrap-icons';
import positiveImg from './thumbs-up.png';
import negativeImg from './thumbs-down.png';


class AnalyzeTweet extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            result: ""
        }
    }

    reset() {
        this.setState({
            sentiment: "",
            score: ""
        })
    }

    analyzeTweet(msg) {
        console.log(msg)

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ inputTweet: msg })
        };

        fetch("http://127.0.0.1:5000/sentiment", requestOptions).then(res => res.json()).then(res => {
            console.log(res)
            this.setState({ sentiment: res.sentiment, score: res.score })
        }, (error) => { alert(" error while fetching..") })
    }


    render() {
        if(this.state.sentiment) {
            return (
                <Container  className="justify-content-md-center" fluid>
                    <Card style={{ width: '18rem' }}>
                        <HandThumbsUpFill className="bi bi-align-center" color="limegreen" size={96} title="positive" />
                        <Card.Body>
                            <Card.Title>{this.state.sentiment}</Card.Title>
                            <Card.Text>
                                This is an example explanation for why the decision was made to be positive.
                                Maybe we could include which words impacted this decsion?
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Container>
        );
        } else {
            return (
                <Container class="resultsContainer" fluid>
                    <Card style={{ width: '18rem' }}>
                        <Card.Img variant="top" class="rounded mx-auto d-block" src={positiveImg} />
                        <Card.Body>
                            <Card.Title>Positive or Negative?</Card.Title>
                            <Card.Text>
                                This is an example explanation for why the decision was made to be positive.
                                Maybe we could include which words impacted this decsion?
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Container>
            );
        }
        
    }
}

export default AnalyzeTweet;