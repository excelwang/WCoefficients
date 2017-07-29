# WCoefficients
Solver of W Coefficients

## Input
the largest n to be solved

## Output
### n,k,W coefficients

1,1,W<sub>1</sub><sup>1,1</sup>

2,1,W<sub>1</sub><sup>2,1</sup>, W<sub>2</sub><sup>2,1</sup>

2,2,W<sub>1</sub><sup>2,2</sup>, W<sub>2</sub><sup>2,2</sup>, 

3,1,W<sub>1</sub><sup>3,1</sup>,W<sub>2</sub><sup>3,1</sup>,W<sub>3</sub><sup>3,1</sup>

...

n,n-1,W<sub>1</sub><sup>n,n-1</sup>,W<sub>2</sub><sup>n,n-1</sup>,...,W<sub>n</sub><sup>n,n-1</sup>

n,n,W<sub>1</sub><sup>n,n</sup>,W<sub>2</sub><sup>n,n</sup>,...,W<sub>n</sub><sup>n,n</sup>
## Document/Paper
Citing the paper is better:
https://arxiv.org/abs/1707.08860

## Some Frequently Used W Coefficients (W<sup>n,k</sup><sub>i</sub>)
<TABLE>
<tr><td>W<sup>1,1</sup><sub>1</sub>: 1	</td><td>W<sup>6,1</sup><sub>2</sub>: -15	</td><td>W<sup>7,3</sup><sub>7</sub>: 15	</td><td>W<sup>8,5</sup><sub>8</sub>: -35	</td><td>W<sup>9,4</sup><sub>7</sub>: -720	</td><td>W<sup>10,3</sup><sub>3</sub>: 120	</td></tr>
<tr><td>W<sup>2,1</sup><sub>1</sub>: 2	</td><td>W<sup>6,1</sup><sub>3</sub>: 20	</td><td>W<sup>7,4</sup><sub>4</sub>: 35	</td><td>W<sup>8,5</sup><sub>5</sub>: 56	</td><td>W<sup>9,4</sup><sub>8</sub>: 315	</td><td>W<sup>10,3</sup><sub>4</sub>: -630	</td></tr>
<tr><td>W<sup>2,1</sup><sub>2</sub>: -1	</td><td>W<sup>6,1</sup><sub>4</sub>: -15	</td><td>W<sup>7,4</sup><sub>5</sub>: -84	</td><td>W<sup>8,5</sup><sub>6</sub>: -140	</td><td>W<sup>9,4</sup><sub>9</sub>: -56	</td><td>W<sup>10,3</sup><sub>5</sub>: 1512	</td></tr>
<tr><td>W<sup>2,1</sup><sub>1</sub>: 0	</td><td>W<sup>6,1</sup><sub>5</sub>: 6	</td><td>W<sup>7,4</sup><sub>6</sub>: 70	</td><td>W<sup>8,5</sup><sub>7</sub>: 120	</td><td>W<sup>9,5</sup><sub>8</sub>: -315	</td><td>W<sup>10,3</sup><sub>6</sub>: -2100	</td></tr>
<tr><td>W<sup>2,2</sup><sub>2</sub>: 1	</td><td>W<sup>6,1</sup><sub>6</sub>: -1	</td><td>W<sup>7,4</sup><sub>7</sub>: -20	</td><td>W<sup>8,6</sup><sub>8</sub>: 21	</td><td>W<sup>9,5</sup><sub>9</sub>: 70	</td><td>W<sup>10,3</sup><sub>7</sub>: 1800	</td></tr>
<tr><td>W<sup>3,1</sup><sub>1</sub>: 3	</td><td>W<sup>6,2</sup><sub>2</sub>: 15	</td><td>W<sup>7,5</sup><sub>5</sub>: 21	</td><td>W<sup>8,6</sup><sub>6</sub>: 28	</td><td>W<sup>9,5</sup><sub>5</sub>: 126	</td><td>W<sup>10,3</sup><sub>8</sub>: -945	</td></tr>
<tr><td>W<sup>3,1</sup><sub>2</sub>: -3	</td><td>W<sup>6,2</sup><sub>3</sub>: -40	</td><td>W<sup>7,5</sup><sub>6</sub>: -35	</td><td>W<sup>8,6</sup><sub>7</sub>: -48	</td><td>W<sup>9,5</sup><sub>6</sub>: -420	</td><td>W<sup>10,3</sup><sub>9</sub>: 280	</td></tr>
<tr><td>W<sup>3,1</sup><sub>3</sub>: 1	</td><td>W<sup>6,2</sup><sub>4</sub>: 45	</td><td>W<sup>7,5</sup><sub>7</sub>: 15	</td><td>W<sup>8,7</sup><sub>8</sub>: -7	</td><td>W<sup>9,5</sup><sub>7</sub>: 540	</td><td>W<sup>10,3</sup><sub>10</sub>: -36	</td></tr>
<tr><td>W<sup>3,2</sup><sub>2</sub>: 3	</td><td>W<sup>6,2</sup><sub>5</sub>: -24	</td><td>W<sup>7,6</sup><sub>6</sub>: 7	</td><td>W<sup>8,7</sup><sub>7</sub>: 8	</td><td>W<sup>9,6</sup><sub>8</sub>: 189	</td><td>W<sup>10,4</sup><sub>4</sub>: 210	</td></tr>
<tr><td>W<sup>3,2</sup><sub>3</sub>: -2	</td><td>W<sup>6,2</sup><sub>6</sub>: 5	</td><td>W<sup>7,6</sup><sub>7</sub>: -6	</td><td>W<sup>8,8</sup><sub>8</sub>: 1	</td><td>W<sup>9,6</sup><sub>9</sub>: -56	</td><td>W<sup>10,4</sup><sub>5</sub>: -1008	</td></tr>
<tr><td>W<sup>3,3</sup><sub>3</sub>: 1	</td><td>W<sup>6,3</sup><sub>3</sub>: 20	</td><td>W<sup>7,7</sup><sub>7</sub>: 1	</td><td>W<sup>9,1</sup><sub>1</sub>: 9	</td><td>W<sup>9,6</sup><sub>6</sub>: 84	</td><td>W<sup>10,4</sup><sub>6</sub>: 2100	</td></tr>
<tr><td>W<sup>4,1</sup><sub>1</sub>: 4	</td><td>W<sup>6,3</sup><sub>4</sub>: -45	</td><td>W<sup>8,1</sup><sub>1</sub>: 8	</td><td>W<sup>9,1</sup><sub>2</sub>: -36	</td><td>W<sup>9,6</sup><sub>7</sub>: -216	</td><td>W<sup>10,4</sup><sub>7</sub>: -2400	</td></tr>
<tr><td>W<sup>4,1</sup><sub>2</sub>: -6	</td><td>W<sup>6,3</sup><sub>5</sub>: 36	</td><td>W<sup>8,1</sup><sub>2</sub>: -28	</td><td>W<sup>9,1</sup><sub>3</sub>: 84	</td><td>W<sup>9,7</sup><sub>8</sub>: -63	</td><td>W<sup>10,4</sup><sub>8</sub>: 1575	</td></tr>
<tr><td>W<sup>4,1</sup><sub>3</sub>: 4	</td><td>W<sup>6,3</sup><sub>6</sub>: -10	</td><td>W<sup>8,1</sup><sub>3</sub>: 56	</td><td>W<sup>9,1</sup><sub>4</sub>: -126	</td><td>W<sup>9,7</sup><sub>9</sub>: 28	</td><td>W<sup>10,4</sup><sub>9</sub>: -560	</td></tr>
<tr><td>W<sup>4,1</sup><sub>4</sub>: -1	</td><td>W<sup>6,4</sup><sub>4</sub>: 15	</td><td>W<sup>8,1</sup><sub>4</sub>: -70	</td><td>W<sup>9,1</sup><sub>5</sub>: 126	</td><td>W<sup>9,7</sup><sub>7</sub>: 36	</td><td>W<sup>10,4</sup><sub>10</sub>: 84	</td></tr>
<tr><td>W<sup>4,2</sup><sub>2</sub>: 6	</td><td>W<sup>6,4</sup><sub>5</sub>: -24	</td><td>W<sup>8,1</sup><sub>5</sub>: 56	</td><td>W<sup>9,1</sup><sub>6</sub>: -84	</td><td>W<sup>9,8</sup><sub>8</sub>: 9	</td><td>W<sup>10,5</sup><sub>5</sub>: 252	</td></tr>
<tr><td>W<sup>4,2</sup><sub>3</sub>: -8	</td><td>W<sup>6,4</sup><sub>6</sub>: 10	</td><td>W<sup>8,1</sup><sub>6</sub>: -28	</td><td>W<sup>9,1</sup><sub>7</sub>: 36	</td><td>W<sup>9,8</sup><sub>9</sub>: -8	</td><td>W<sup>10,5</sup><sub>6</sub>: -1050	</td></tr>
<tr><td>W<sup>4,2</sup><sub>4</sub>: 3	</td><td>W<sup>6,5</sup><sub>5</sub>: 6	</td><td>W<sup>8,1</sup><sub>7</sub>: 8	</td><td>W<sup>9,1</sup><sub>8</sub>: -9	</td><td>W<sup>9,9</sup><sub>9</sub>: 1	</td><td>W<sup>10,5</sup><sub>7</sub>: 1800	</td></tr>
<tr><td>W<sup>4,3</sup><sub>3</sub>: 4	</td><td>W<sup>6,5</sup><sub>6</sub>: -5	</td><td>W<sup>8,1</sup><sub>8</sub>: -1	</td><td>W<sup>9,1</sup><sub>9</sub>: 1	</td><td>W<sup>10,1</sup><sub>1</sub>: 10	</td><td>W<sup>10,5</sup><sub>8</sub>: -1575	</td></tr>
<tr><td>W<sup>4,3</sup><sub>4</sub>: -3	</td><td>W<sup>6,6</sup><sub>6</sub>: 1	</td><td>W<sup>8,2</sup><sub>2</sub>: 28	</td><td>W<sup>9,2</sup><sub>2</sub>: 36	</td><td>W<sup>10,1</sup><sub>2</sub>: -45	</td><td>W<sup>10,5</sup><sub>9</sub>: 700	</td></tr>
<tr><td>W<sup>4,4</sup><sub>4</sub>: 1	</td><td>W<sup>7,1</sup><sub>1</sub>: 7	</td><td>W<sup>8,2</sup><sub>3</sub>: -112	</td><td>W<sup>9,2</sup><sub>3</sub>: -168	</td><td>W<sup>10,1</sup><sub>3</sub>: 120	</td><td>W<sup>10,5</sup><sub>10</sub>: -126	</td></tr>
<tr><td>W<sup>5,1</sup><sub>1</sub>: 5	</td><td>W<sup>7,1</sup><sub>2</sub>: -21	</td><td>W<sup>8,2</sup><sub>4</sub>: 210	</td><td>W<sup>9,2</sup><sub>4</sub>: 378	</td><td>W<sup>10,1</sup><sub>4</sub>: -210	</td><td>W<sup>10,6</sup><sub>8</sub>: 945	</td></tr>
<tr><td>W<sup>5,1</sup><sub>2</sub>: -10	</td><td>W<sup>7,1</sup><sub>3</sub>: 35	</td><td>W<sup>8,2</sup><sub>5</sub>: -224	</td><td>W<sup>9,2</sup><sub>5</sub>: -504	</td><td>W<sup>10,1</sup><sub>5</sub>: 252	</td><td>W<sup>10,6</sup><sub>9</sub>: -560	</td></tr>
<tr><td>W<sup>5,1</sup><sub>3</sub>: 10	</td><td>W<sup>7,1</sup><sub>4</sub>: -35	</td><td>W<sup>8,2</sup><sub>6</sub>: 140	</td><td>W<sup>9,2</sup><sub>6</sub>: 420	</td><td>W<sup>10,1</sup><sub>6</sub>: -210	</td><td>W<sup>10,6</sup><sub>10</sub>: 126	</td></tr>
<tr><td>W<sup>5,1</sup><sub>4</sub>: -5	</td><td>W<sup>7,1</sup><sub>5</sub>: 21	</td><td>W<sup>8,2</sup><sub>7</sub>: -48	</td><td>W<sup>9,2</sup><sub>7</sub>: -216	</td><td>W<sup>10,1</sup><sub>7</sub>: 120	</td><td>W<sup>10,6</sup><sub>6</sub>: 210	</td></tr>
<tr><td>W<sup>5,1</sup><sub>5</sub>: 1	</td><td>W<sup>7,1</sup><sub>6</sub>: -7	</td><td>W<sup>8,2</sup><sub>8</sub>: 7	</td><td>W<sup>9,2</sup><sub>8</sub>: 63	</td><td>W<sup>10,1</sup><sub>8</sub>: -45	</td><td>W<sup>10,6</sup><sub>7</sub>: -720	</td></tr>
<tr><td>W<sup>5,2</sup><sub>2</sub>: 10	</td><td>W<sup>7,1</sup><sub>7</sub>: 1	</td><td>W<sup>8,3</sup><sub>3</sub>: 56	</td><td>W<sup>9,2</sup><sub>9</sub>: -8	</td><td>W<sup>10,1</sup><sub>9</sub>: 10	</td><td>W<sup>10,7</sup><sub>8</sub>: -315	</td></tr>
<tr><td>W<sup>5,2</sup><sub>3</sub>: -20	</td><td>W<sup>7,2</sup><sub>2</sub>: 21	</td><td>W<sup>8,3</sup><sub>4</sub>: -210	</td><td>W<sup>9,3</sup><sub>3</sub>: 84	</td><td>W<sup>10,1</sup><sub>10</sub>: -1	</td><td>W<sup>10,7</sup><sub>9</sub>: 280	</td></tr>
<tr><td>W<sup>5,2</sup><sub>4</sub>: 15	</td><td>W<sup>7,2</sup><sub>3</sub>: -70	</td><td>W<sup>8,3</sup><sub>5</sub>: 336	</td><td>W<sup>9,3</sup><sub>4</sub>: -378	</td><td>W<sup>10,2</sup><sub>2</sub>: 45	</td><td>W<sup>10,7</sup><sub>10</sub>: -84	</td></tr>
<tr><td>W<sup>5,2</sup><sub>5</sub>: -4	</td><td>W<sup>7,2</sup><sub>4</sub>: 105	</td><td>W<sup>8,3</sup><sub>6</sub>: -280	</td><td>W<sup>9,3</sup><sub>5</sub>: 756	</td><td>W<sup>10,2</sup><sub>3</sub>: -240	</td><td>W<sup>10,7</sup><sub>7</sub>: 120	</td></tr>
<tr><td>W<sup>5,3</sup><sub>3</sub>: 10	</td><td>W<sup>7,2</sup><sub>5</sub>: -84	</td><td>W<sup>8,3</sup><sub>7</sub>: 120	</td><td>W<sup>9,3</sup><sub>6</sub>: -840	</td><td>W<sup>10,2</sup><sub>4</sub>: 630	</td><td>W<sup>10,8</sup><sub>8</sub>: 45	</td></tr>
<tr><td>W<sup>5,3</sup><sub>4</sub>: -15	</td><td>W<sup>7,2</sup><sub>6</sub>: 35	</td><td>W<sup>8,3</sup><sub>8</sub>: -21	</td><td>W<sup>9,3</sup><sub>7</sub>: 540	</td><td>W<sup>10,2</sup><sub>5</sub>: -1008	</td><td>W<sup>10,8</sup><sub>9</sub>: -80	</td></tr>
<tr><td>W<sup>5,3</sup><sub>5</sub>: 6	</td><td>W<sup>7,2</sup><sub>7</sub>: -6	</td><td>W<sup>8,4</sup><sub>8</sub>: 35	</td><td>W<sup>9,3</sup><sub>8</sub>: -189	</td><td>W<sup>10,2</sup><sub>6</sub>: 1050	</td><td>W<sup>10,8</sup><sub>10</sub>: 36	</td></tr>
<tr><td>W<sup>5,4</sup><sub>4</sub>: 5	</td><td>W<sup>7,3</sup><sub>3</sub>: 35	</td><td>W<sup>8,4</sup><sub>4</sub>: 70	</td><td>W<sup>9,3</sup><sub>9</sub>: 28	</td><td>W<sup>10,2</sup><sub>7</sub>: -720	</td><td>W<sup>10,9</sup><sub>9</sub>: 10	</td></tr>
<tr><td>W<sup>5,4</sup><sub>5</sub>: -4	</td><td>W<sup>7,3</sup><sub>4</sub>: -105	</td><td>W<sup>8,4</sup><sub>5</sub>: -224	</td><td>W<sup>9,4</sup><sub>4</sub>: 126	</td><td>W<sup>10,2</sup><sub>8</sub>: 315	</td><td>W<sup>10,9</sup><sub>10</sub>: -9	</td></tr>
<tr><td>W<sup>5,5</sup><sub>5</sub>: 1	</td><td>W<sup>7,3</sup><sub>5</sub>: 126	</td><td>W<sup>8,4</sup><sub>6</sub>: 280	</td><td>W<sup>9,4</sup><sub>5</sub>: -504	</td><td>W<sup>10,2</sup><sub>9</sub>: -80	</td><td>W<sup>10,10</sup><sub>10</sub>: 1	</td></tr>
<tr><td>W<sup>6,1</sup><sub>1</sub>: 6	</td><td>W<sup>7,3</sup><sub>6</sub>: -70	</td><td>W<sup>8,4</sup><sub>7</sub>: -160	</td><td>W<sup>9,4</sup><sub>6</sub>: 840	</td><td>W<sup>10,2</sup><sub>10</sub>: 9	</td><td></td></tr>
</TABLE>
