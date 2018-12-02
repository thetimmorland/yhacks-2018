import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import LinearProgress from '@material-ui/core/LinearProgress';
import Image from './sailing.jpg';
import mapImage from './maps.jpeg';
import boatImage from './boat.png';

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
    width: "195px",
  },
  paper: {
    textAlign: 'center',
    width: '250px',
    height: '485px',
    justify: 'center', 
  }, 
  input: {
    direction:"column",
    alignItems:"center",
    justify:"center",
    marginTop: "50px",
  },
  nameField: {
    marginLeft: -10,
    marginRight: 80,
    textAlight: 'center',
  },
  titlein: {
    textAlign: 'center',
    justif: 'center',
    height: '55px',
    justify: 'center',
  },
  titleout: {
    backgroundColor: '#121858',
  },
  backContainer: { 
    backgroundImage: `url(${Image})`,
    width: '100%',
    height: '800px',
    justify: 'center',
    backgroundSize: 'cover',
  },
  paper2: {
    textAlign: 'center',
    width: '500px',
    height: '500px',
    backgroundImage: `url(${mapImage})`,
    marginTop: "4%",
  },
});

function Index(props) {
  const { classes } = props;
  return (
    <div>
      <body className={classes.backContainer}>
        <AppBar position="static" className={classes.spacer}>
          <Toolbar className = {classes.titleout}>
            <img className = {classes.boat} src={boatImage} height="50" width="50" />
            <Typography variant = 'h3' color='inherit' className = {classes.titlein}>
             Sailon
            </Typography>
          </Toolbar>
        </AppBar>
        <LinearProgress color="primary" variant="query" />
        <Grid className={classes.input} container justify = "center" container spacing={24}>
          <Grid  item xs={20} position="static">
            <Paper className={classes.paper2}>
            </Paper>
          </Grid>
          <Grid item xs={3} position="static">
            <Paper className={classes.paper}>
              <form className={classes.container} noValidate autoComplete="off">
                <p className={classes.spacer}></p>
                <p><br></br>Please enter the following information correctly <br></br>[North +, East +]: </p>
                <TextField
                  id="initialLong"
                  label="Initial Longitude"
                  className={classes.textField}
                  margin="normal"
                  variant="outlined"
                />
                <TextField
                  id="inititalLad"
                  label="Initial Latitude"
                  className={classes.textField}
                  margin="normal"
                  variant="outlined"
                /> 
                <TextField
                 id="finalLong"
                  label="Final Longitude"
                  className={classes.textField}
                  margin="normal" 
                  variant="outlined"
                />
                <TextField
                  id="finalLat"
                  label="Final Latitude"
                  className={classes.textField}
                  margin="normal"
                  variant="outlined"
                />
                </form>
              <Button variant="contained" color="primary" className={classes.button}>
              Sail
              </Button>
              <p className = {classes.spacer}></p>
              <LinearProgress color="secondary" variant="query" />
            </Paper>
          </Grid>
        </Grid>
      </body>
    </div>
    )
  }

Index.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Index);