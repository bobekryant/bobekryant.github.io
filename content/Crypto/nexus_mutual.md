Title: Nexus Mutual 
Slug: nexus-mutual-insurance
Date: 2020-08-19
Tags: crypto, trading, DeFi, $NXM
Summary: Insurance for the every growing crypto space.

<h3>Introduction</h3>
<p>
Decentralized finance, DeFi, is the hottest subsection in crypto right now and is one of the main driving forces behind this current the bull market. 
In this space I have two tokens with high conviction, Nexus Mutual, \$NXM, and Yearn Finance, \$YFI and I will be sharing my thesis for Nexus Mutual below.
Here is an outline of the article:
<ul>
  <li>The use case for \$NXM.</li>
  <li>The tokenomics and pricing model behind \$NXM.</li>
  <li>Alternative data and price predictions.</li>
  <li>Recent protocol changes and why I am so bullish on it.</li>
</ul>
</p>


<h3>DeFi</h3>
<p>
The main principles of DeFi are to rebuild the financial system in a more fair, equitable, and transparent fashion.
Visible and auditied immutable smart contracts deployed so users can trust the system and underlying code.
There are many startups tackling various problems across the entire DeFi stack.
Currently, the projects in DeFi with the highest market cap are trading (decentralized exchanges) and yield farming (lending).
Smaller projects include prediction markets and payments are also popular.
</p>

<p>
The amount of assets in this space has seen staggering growth in the past few months. 
A popular metric to measure this growth is TVL or total value locked.
This translates to the sum of the value of the assets in the various DeFi platforms.
Below is a picture of the TVL for the past year from <a href="https://defipulse.com/" target="_blank">DeFi Pulse</a>.
We can see that the TVL had a steady increase from March to July, but since then the TVL has taken off like a rocket ship, going from 2B in assets to over 6B.
[ref]This chart is slightly misleading as most crypto assets have increased substantially this month so the dollar value would appreciate regardless.
Looking at this chart in terms of \$BTC or \$ETH value is a more accurate representation of asset growth.[/ref]
[ref]There often is an issue with double counting in DeFi, as some coins can be used by multiple protocols.[/ref]
</p>

<center>
![Pelican2](../images/crypto/tvl_defi.PNG)
</center>

<h3>NXM Use Case: Insurance</h3>
<p>
At the heart of DeFi is the reliance of smart contract protocols and Nexus Mutual provides insurance on all of the underlying code to protect users from bugs in these contracts. 
Nexus Mutual is the first and largest insurance provider in the DeFi space. 
The current smart contracts in Nexus Mutual cover the popular DeFi tokens such as \$CRV, \$YFI, \$SNX, and \$LEND.
Members of the mutual are able to use the \$NXM token to provide coverage of smart contracts, purchase coverage of smart contracts, and participate in claims assessment and risk assessment. 
The \$NXM token can be purchased <a href="https://app.nexusmutual.io/exchange" target="_blank">here</a>[ref]Will need to KYC to purchase \$NXM. One can also buy \$WNXM for exposure to the \$NXM price movements.[/ref]
on the Nexus Mutual exchange.
</p>

<p>
If DeFi grows, Nexus Mutual should also grow as people want to exposure to this space, but need to cap downside risk.
Below is a scatter plot which shows the empirical relationship of the TVL in DeFi to the Nexus Mutual capital pool (amount of assets in the mutual).
The data starts in July 23, 2019 and goes to present day.
Although the data is noisy, as each data point is a day, there is a strong linear and then exponential trend between the two variables. 
</p>

<center>
![Pelican2](../images/crypto/defi_tvl_nxm_cp.PNG)
</center>


<h3>NXM Pricing Model</h3>
<p>
\$NXM does not follow normal free market pricing like the other tokens. It has a continuous token model also known as a bonding curve.
This means that the price is formulaic and varies based on two main parameters:

<ol>
  <li>Funding level of mutual</li>
  <li>Amount of capital required to cover claims</li>
</ol>

In the short term, the funding level of the mutual matters as this impacts the immediate financial position and encourages new money when funding is low.
For the long term, the required capital rises to reflect platform adoption.
</p>


<h5>NXM Pricing Model: Bonding Curve Formula</h5>
<p>
The bonding curve formula is a little complicated and I will walk through various scenarios and show impact on price[ref]The \$NXM price is currently pegged to the price of \$ETH.[/ref].
First the formula and some definitions:
</p>

\begin{align}
TP &= A+\frac{MCR}{C}MCR\%^4 \\
\text{where} & \\
TP &= \text{Token Price in Ether} \\
A &= 0.01028 \text{; This is a constant calibrated at launch} \\
MCR &= \text{Value of Minimum Capital Requirement in Ether} \\
C &= 5,800,000 \text{; This is a constant calibrated at launch} \\
MCR\% &= \text{Ratio of Capital Pool to Minimum Capital Requirement} \\
\end{align}

<p>
Note that the price of \$NXM is inherently pegged to the price of \$ETH and holding \$NXM also has \$ETH underlying exposure.
As we can see, there are two main variables which decide the price: MCR and MCR%. 
MCR% is broken down into the numerator, capital pool, and denominator MCR.
The capital pool is the total capital for Nexus Mutual to be able to pay out covers in case of black swan event and increases when people purchase \$NXM.
</p>

<p>
Before going further into the math of the bonding curve, I want to point out why \$NXM is such an interesting token: it has a built in asymmetric risk reward opportunity.
Entering at certain times, the downside risk is capped and the upside risk grows exponentially.
I will explain the calculations and thought process that led me to this conclusion below.
</p>

<h5>NXM Pricing Model: MCR</h5>
<p>
The MCR is determined by the capital model
[ref]The actual formula is created by the European Insurance and Occupational Pensions Authority with two components, a best estimate liability which is the expected loss on each contract cover, and a buffer for a black swan event.[/ref]
and is set to achieve a 99.5% probability of solvency over a 1 year period.
MCR increases gradually as people are buying \$NXM and it is set at a minimum of 7000 \$ETH.
MCR increases by 1% everyday that MCR% is greater than 130%.
Note that MCR can only increase and never decrease and this feature intrinsically creates a base price for the \$NXM token. 
</p>

$\frac{MCR}{C}$ is the long term portion of the formula. 
Because C is a constant and MCR can only go up, over the long run the tokenomics dictate that the price should slowly rise.
If the price of \$NXM goes down it is due to the short run portion of the model.

<h5>NXM Pricing Model: MCR%</h5>
<p>
MCR% is the short term portion of the formula and because MCR% is raised to the power of 4, small changes in MCR% can cause large ripple effects in the price.
It is important to note the tokenomics in play when looking at MCR%. Whenever MCR increases, MCR% will decrease, because MCR is on the denominator. 
This decrease will also have a larger decrease in the price of NXM and will override the long term MCR base increase because of scaling factor.

\begin{align}
MCR\% &= \frac{CP}{MCR}\\
\text{where} & \\
MCR\% &= \text{Ratio of Capital Pool to Minimum Capital Requirement} \\
CP &= \text{Capital Pool} \\
MCR &= \text{Value of Minimum Capital Requirement in Ether} \\
\end{align}
</p>

<h5>NXM Pricing Model: MCR and MCR% Interaction</h5>
<p>
If there is more capital flowing into Nexus Mutual than MCR increases, then MCR% will go up and \$NXM price will also rise.
The baseline model has MCR increasing by 1% every 24 hours so long as MCR% is larger than 130%. 
This means that capital must flow into the mutual more than 1% of MCR each 24 hours or the price of \$NXM will go down.
</p>

<h5>NXM Pricing Model: Restrictions</h5>
<p>
There are a few restrictions in the pricing model:
<ol>
  <li>Capital Pool must be above the MCR, so MCR% cannot drop below 100.</li>
  <li>Redemptions are capped per transaction.</li>
  <li>Bid ask spread for \$NXM is 2.5% on the \$NXM exchange.</li>
  <li>Only members of mutual can own NXM tokens. Other addresses are whitelisted.</li>
</ol>
</p>

<h5>NXM Pricing Model: Data</h5>
<p>
I have created a <a href="https://docs.google.com/spreadsheets/d/1CtkbpzEsyMZAEJfdxL-4i4QKHVutKOohg7Rfd0GlwXM/edit?usp=sharing" target="_blank">Google Sheet</a> to help better visualize the price of \$NXM as MCR and MCR% change.
In addition, here is a graph which sets the lines as the MCR and then shows price of \$NXM in \$ETH on the y-axis with the MCR% on the x-axis.
We can see that the price increases exponentially as the MCR% changes and shifts up wards while keeping MCR constant. 
MCR only goes up and has linear movements, while MCR% has exponential movements on the upside, but can go up or down.
</p>

<center>
![Pelican2](../images/crypto/nxm_bonding_curve.png)
</center>

<p>
To highlight the bonding curve formula more vividly, here is an example. 
Over the next year, if MCR% does not change, MCR will keep on increasing by 1% a day which will translate to \$NXM price increasing more than 37x.
If MCR% gradually falls to 130% and remains there, then \$NXM price will increase by around 16x.
If MCR% falls to 100% and stays there for a year, \$NXM will drop by around a factor of 7.
I believe in stacking asymmetric bets and \$NXM presents one of the most asymmetric bets I have seen in crypto in a while.
</p>

<h3>Alternative Data</h3>
<p>
There are a few key performance metrics that exist to determine if the mutual is growing or shrinking and try to predict the future price of \$NXM.
These indicators include capital pool increases and amount staked.
</p>

<h5>Capital Pool</h5>
<p>
I mentioned this in the previous section, but it is worth repeating: capital must flow into the mutual at a rate greater than 1% of MCR each 24 hours or the price of \$NXM will go down. 
Since the MCR is increasing daily as long as MCR% is above 130, everyday more capital must flow into mutual than previous day to keep MCR% the same and increase the price of \$NXM.
For example, if the MCR were to be 100k \$ETH and the MCR% was over 130%, the capital pool would need to increase by around 1k every day to maintain the MCR%.
</p>

<p>
I have tracked the capital pool data and plotted below.
Since July, the capital pool has gone parabolic. Each day over 2500 \$ETH has been added to the pool.
</p>

<center>
![Pelican2](../images/crypto/nxm_capital_pool.png)
</center>

<h5>Staking</h5>
<p>
Any member of the mutual can stake their \$NXM tokens on protocols to earn rewards. If there is an accepted claim on that protocol, the 
$NXM staked is burned and paid out. 
\$NXM staking locks the tokens in the system for at least 90 days, which makes the tokens sticky and creates a baseline of tokens in the system. 
Currently there are around 140 million dollars staked and with a market cap of around 210 million, this means that around 66% of the \$NXM tokens in circulation are locked and cannot be used to speculate in the short term.
Increasing the amount staked, especially in proportion to the total amount of \$NXM tokens is bullish for the price of \$NXM as those cannot be swapped for \$ETH.
</p>




<h3>Protocol Change: Governance Vote</h3>
<p>
Due to the explosion in DeFi, there ended up being more demand for cover than capital in Nexus Mutual, resulting in not enough capacity; because the capacity is limited by the MCR. 
Previously, MCR was bounded to at most increase by 1% per day if mutual has 'excess capital' of funds above 130% of MCR.
On July 9th, the NXM community submitted a protocol change.
Governance proposal <a href="https://forum.nexusmutual.io/t/capital-scaling/63" target="_blank">83</a> helped relieve the issue of a low MCR by reducing the  MCR incremental time from 1 day to 4 hours necessary to increase MCR 1% if over the 130% MCR cap.
This would revert back to once per day when the MCR reaches 100k ETH.
</p>

<p>
This change allowed the mutual to attract capital faster and benefit from scaling faster.
In essence, by looking at the pricing curve, we can see that this was a short term trade off for a long term gain. 
As long as MCR% is over 130, MCR would increase by 6% per day instead of 1% per day.
By enacting the change, the MCR portion of the formula will increase 6 times faster, but made it very hard for the MCR% portion of the formula to increase.
I have a chart of the MCR below and it is easy to see the MCR immediately spike from this protocol adjustment. 
At the current rate, Nexus Mutual will hit 100k \$ETH MCR around August 21st and then the MCR will go back to only increasing once per day.
</p>

<center>
![Pelican2](../images/crypto/nxm_mcr.png)
</center>

<p>
Previously to maintain the MCR%, over 6k \$ETH needed to be deposited daily. 
However, at 100k \$ETH MCR, this is cut by a factor of 6 and only a little over 1k \$ETH needs to be deposited daily to maintain the price.
Anymore deposits would create an increase in MCR% pushing the price to a parabolic portion of the bonding curve.
Just in the month of August there have been almost 8k \$ETH deposited daily. 
Thus due to this protocol change, if the mutual can even maintain half as much deposits as earlier in August, the \$NXM price will go exponential.
</p>

<h3>Protocol Change: Investing</h3>
<p>
It has been hinted at a few times on the website and throughout various sources, Nexus Mutual will invest its assets to generate additional yield for its members.
There are many ways to generate additional profits with the large base capital, but this process is similar to how tradition insurance companies invest their funds.
</p>

<h3>Trading</h3>
<p>
There are two short term opportunities to make even more money in \$NXM: arbitrage and front running. 
These are high conviction bets whose profits can be recycled back into the trades as there is decent volume.
</p>

<h5>Arbitrage</h5>
<p>
To buy \$NXM, it is necessary to KYC on the Nexus Mutual website. Nexus Mutual then whitelists a wallet address where one can freely convert \$NXM to \$ETH and back.
For those who do not want to \$KYC, they can purchase \$WNXM, which is a wrapped based around the \$NXM token. 
Each \$WNXM is redeemable <a href="https://je45e4c2q4x52s66qenp5aeyfonfsvkvupkf4ipefkzs364gbera.arweave.net/STnScFqHL91L3oEa_oCYK5pZVVWj1F4h5CqzLfuGCSI/#/" target="_blank">here</a> for a \$NXM and the process can be reversed.
The \$WNXM token trades on multiple exchanges and any time these prices differ by a certain amount, people can make money bringing these prices back in line.
Price differences will mostly occur when MCR% is high (more volatile prices) or everyday during the rebalance when the MCR changes.
</p>
<h5>Frontrunning</h5>
<p>
I hinted at this above, but the daily MCR change can be easily frontrun. The price of \$NXM will temporarily decrease everyday at 14:00, which forces the price to go down. 
Take the scenario where we have MCR% at 131% and MCR at 100k \$ETH, making capital pool 131k \$ETH, and creating a price of 0.0611 \$ETH from the bonding curve.
At 14:00, the MCR changes to 101k \$ETH and MCR% then drops to 129.7%, giving a price of .0596 \$ETH from the bonding curve, a difference of almost 2.5%.
</p>

<h3>Risks</h3>
<p>
Putting in money in Nexus Mutual is not risk free. 
If there is a large payout event then the capital pool would get hammered causing a large drop in MCR%. 
In February, Nexus Mutual <a href="https://www.coindesk.com/defi-insurance-firm-nexus-mutual-makes-its-first-payout-following-bzx-attacks" target="_blank">paid out</a> its first claim.
The current largest insurance claims are for the Curve stablecoin and BTC pools (25k \$ETH) and Yearn (20k \$ETH). 
Paying out these covers would cripple \$NXM price in the short term and would see MCR% ranging from 100% to 130%.
Finally, current MCR% is high and the risk-reward tradeoff would be a lot higher to buy NXM when the MCR% is closer to the 130% mark.
</p>

<h3>Conclusions</h3>
<p>
\$NXM presents a great opportunity to invest in a company with clear use-case for the growing DeFi landscape.
In order to stake the tokens, I would need to be more familiar with the code of these protocols, but \$NXM stands out as a clear winner in the space whose price will appreciate as DeFi grows. 
I have accumulated a position of \$NXM to hold while also taking advantage of the tokenomics to trade in and out of shorter term positions.
</p>
