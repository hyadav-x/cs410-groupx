import React from "react";
import Container from "react-bootstrap/esm/Container";
import Spinner from "react-bootstrap/Spinner";
import { Card } from "react-bootstrap";
import positiveImg from './thumbs-up.png';
import negativeImg from './thumbs-down.png';


class AnalyzeTweet extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            sentiment: "",
            score: "",
            loading: false
        }
    }

    reset() {
        this.setState({
            sentiment: "",
            score: "",
            loading: false
        })
    }

    analyzeTweet(msg) {
        console.log(msg)

        this.setState({
            sentiment: "",
            score: "",
            loading: true
        })

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ inputTweet: msg })
        };

        fetch("http://localhost:5000/sentiment", requestOptions).then(res => res.json()).then(res => {
            console.log(res)
            this.setState({ sentiment: res.sentiment, score: res.score, loading: false })
        }, (error) => { alert("Error occurred while fetching the response..") })
    }


    render() {
        if(this.state.loading) {
            return <Spinner animation="border" />;
        }
        if (this.state.sentiment) {
            return (
                <Card style={{ width: '18rem' }}>
                    <Card.Body>
                        <Card.Title>{this.state.sentiment}</Card.Title>
                        <Card.Text>
                            Our model has analyzed your tweet message and resulted in a {this.state.sentiment} sentiment. 
                        </Card.Text>
                        <Card.Img variant="bottom" class="rounded mx-auto d-block" src={this.state.sentiment === "Positive" ? positiveImg : negativeImg} />
                    </Card.Body>
                </Card>
            );
        } else {
            return (
                <Container></Container>
            );
        }

    }
}

export default AnalyzeTweet;